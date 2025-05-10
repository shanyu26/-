"""
使用页面滚动法爬取，每个城市每个岗位最多只有二十页数据。
两种爬取方法都为单线程非异步爬取，故效率并不高。
"""

from DrissionPage import ChromiumPage
from time import sleep
import csv
import pandas

def download(number, city, position):
    k = 0
    dp = ChromiumPage()
    dp.listen.start('/wapi/zpgeek/search/joblist.json?')
    dp.get(f'https://www.zhipin.com/web/geek/jobs?query=&city={city}&position={position}')
    for page in range(1, number+1):

        if k>2:# 多次失败，跳出循环
            break

        r = dp.listen.wait(timeout=2)
        try:
            dic = r.response.body
            data_tem = dic['zpData']['jobList']
            # 将数据写入csv文件中
            # 打开文件
            with open("data/data_boss2.csv",mode='a',encoding='utf-8',newline='') as f_tem:
                csv_write_tem = csv.writer(f_tem)
                # 读入数据
                for item_tem in data_tem:
                    csv_write_tem.writerow(item_tem.values())
            print(f"第{page}页下载完成")
        except:
            print(f"第{page}页下载失败或无数据")
            k += 1
            pass
        dp.scroll.to_bottom()
        sleep(1)


if __name__ == '__main__':
    dp = ChromiumPage()
    dp.get('https://www.zhipin.com/web/geek/jobs?query=&city=101210100&position=100101')
    dp.listen.start('/wapi/zpgeek/search/joblist.json?')
    r = dp.listen.wait()
    dic = r.response.body
    data = dic['zpData']['jobList']
    # 将数据表头写入csv文件中
    # 打开文件
    with open("data/data_boss2.csv", mode='w', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data[0].keys())

    # 读取省份和职位的数据
    city_data = pandas.read_csv("data/city.csv")['code']
    position_data = pandas.read_csv("data/sub_position.scv")['code']
    for position in position_data:
        for city in city_data:
            download(number=20,city=city,position=position) # 翻页最多支持二十页
            print(f"city：{city}，position：{position}下载完成！")
            sleep(3)
    print("over!!!")