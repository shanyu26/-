"""
爬取数据城市，互联网相关职位，以及对应的代码。
使用requests爬取
"""

import requests
import csv
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

def hotCity():
    city_url = 'https://www.zhipin.com/wapi/zpCommon/data/city.json'
    rep_city = requests.get(url=city_url, headers=headers)
    rep_city.encoding = rep_city.apparent_encoding
    dic_city = rep_city.json()
    data = dic_city['zpData']['hotCityList']
    f = open("data/hotCity.csv", mode='w', encoding='utf-8', newline='')
    csv_write = csv.writer(f)
    csv_write.writerow(['code', 'name'])
    for item in data:
        data_temp = [item['code'], item['name']]
        csv_write.writerow(data_temp)

    print("over!!!")
    f.close()
    rep_city.close()

## 请求城市编号
def city():
    city_url = 'https://www.zhipin.com/wapi/zpCommon/data/city.json'
    rep_city = requests.get(url=city_url,headers=headers)
    rep_city.encoding = rep_city.apparent_encoding
    dic_city = rep_city.json()
    data = dic_city['zpData']['cityList']
    f = open("data/province.csv",mode='w',encoding='utf-8',newline='')
    f2 = open("data/city.csv",mode='w',encoding='utf-8',newline='')
    csv_write = csv.writer(f)
    csv_write2 = csv.writer(f2)
    csv_write.writerow(['code','name','rank'])
    csv_write2.writerow(['province_code','code','name','rank'])
    for item in data:
        data_temp = [item['code'],item['name'],item['rank']]
        csv_write.writerow(data_temp)
        for item2 in item['subLevelModelList']:
            data_temp2 = [item['code'], item2['code'], item2['name'], item2['rank']]
            csv_write2.writerow(data_temp2)

    print("over!!!")
    f.close()
    f2.close()
    rep_city.close()

## 请求职位id
def position():
    url_position = "https://www.zhipin.com/wapi/zpCommon/data/getCityShowPosition?cityCode=101120200"
    rep_position = requests.get(url=url_position,headers=headers)
    rep_position.encoding = rep_position.apparent_encoding
    data = rep_position.json()['zpData']['position'][0]['subLevelModelList']
    f = open("data/position.scv",mode='w',encoding='utf-8',newline='')
    f2 = open("data/sub_position.scv",mode='w',encoding='utf-8',newline='')
    csv_write_pos = csv.writer(f)
    csv_write_pos2 = csv.writer(f2)
    csv_write_pos.writerow(['code','name'])
    csv_write_pos2.writerow(['parent_code','code','name'])
    for item in data:
        csv_write_pos.writerow([item['code'],item['name']])
        for item2 in item['subLevelModelList']:
            csv_write_pos2.writerow([item['code'], item2['code'], item2['name']])

    print("over!!")
    f.close()
    f2.close()
    rep_position.close()


if __name__ == '__main__':
    hotCity()