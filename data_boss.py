"""
使用网页爬取，可爬取任意多页，但有封锁IP的风险。
两种爬取方法都为单线程非异步爬取，故效率并不高。
"""

from DrissionPage import ChromiumPage
from time import sleep
import csv
import pandas



def download(number, city, position):
    k = 0
    dp = ChromiumPage()
    dp.get(f'https://www.zhipin.com/web/geek/jobs?query=&city={city}&position={position}')
    dp.listen.start('/wapi/zpgeek/search/joblist.json?')
    for page in range(1, number+1):
        if k>1: # 两次失败，结束爬取
            break

        if page % 5 == 0:
            dp.get(f'https://www.zhipin.com/web/geek/jobs?query=&city={city}&position={position}')
            dp.refresh()
            sleep(3)
            dp.get(f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page={page}&pageSize=15&city={city}&position={position}')
        else:
            dp.get(
                f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page={page}&pageSize=15&city={city}&position={position}')

        r = dp.listen.wait(timeout=2)
        try:
            dic = r.response.body
            data_tem = dic['zpData']['jobList']
            # 将数据写入csv文件中
            # 打开文件
            with open("data/DataBoss_2025-05-10.csv",mode='a',encoding='utf-8',newline='') as f_tem:
                csv_write_tem = csv.writer(f_tem)
                # 读入数据
                for item_tem in data_tem:
                    csv_write_tem.writerow(item_tem.values())
            print(f"第{page}页下载完成")
        except:
            print(f"city：{city}，position：{position}  第{page}页下载失败")
            k += 1
            pass

        sleep(0.5)


if __name__ == '__main__':
    dp = ChromiumPage()
    dp.get('https://www.zhipin.com/web/geek/jobs?query=&city=101210100&position=100101')
    dp.listen.start('/wapi/zpgeek/search/joblist.json?')
    r = dp.listen.wait()
    dic = r.response.body
    data = dic['zpData']['jobList']
    # 将数据表头写入csv文件中
    # 打开文件
    with open("data/DataBoss_2025-05-10.csv", mode='w', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data[0].keys())

    # 读取省份和职位的数据
    city_data = pandas.read_csv("data/hotCity.csv")['code'] # 只爬取热门城市的数据
    position_data = pandas.read_csv("data/sub_position.scv")['code']
    for position in position_data:
        for city in city_data:
            download(number=500,city=city,position=position)
            print(f"city：{city}，position：{position}下载完成！")
            sleep(2)
    print("over!!!")