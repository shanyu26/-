from time import sleep

import requests
import csv
import pandas as pd
headers = {
    "cookie":"lastCity=101120200; b-user-id=5f18687a-0cfe-4c11-ffc0-9dfbf43a7f1f; ab_guid=3cff27d9-9617-49a8-8845-c9a68add9bd9; __g=-; __l=l=%2Fwww.zhipin.com%2Fqingdao%2F%3Fka%3Dheader-home%26seoRefer%3Dindex&r=&g=&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1746673487,1746676856; HMACCOUNT=31384717267B9CB5; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1746676857; __zp_stoken__=b10dfPDjDmcK6wp7Cv0ExFAgMCxRBMzs4LhM2PCw2NT88OEQ7OTw4PBVDLF3Cvh4vY8OPwrrCukElOERCRDxCRDU1FTg4xL%2FDgzk1L1%2FCviczW8OKFx%2FCuGLDl8ODD8OIw4MGw5HCuwtXwrUuKsKAw4E6Q0M%2FY8K7Q8K9D8OCOsK1C8K2Q8OEQzs%2FQzRHDRIMBkc7TE5bDUVgU11bUQlGV0YlPzg4RMKLwp4qOwgQFAgRBQ0RBRQRCQUIERMLDxMKEQkFEQgsPMKhw4PDjsOjw4VTxJXFrMOGwrTFgsO0xKPCjsStw7jEoMKYxKbEg8OPwrXDqcK0w4XCkMOew4PDicK1w6TCtMO8wqbDtsKNw4rDgsOXTsOlwqTDmsKjwpnCrsOvZMOhw4fDvMKhwovCrMOtw4LCrcK7w7DCm8KWwrDCnE%2FDulzCn2bCj8OEwp7Cv8KbbVLDgsK4VsK2TsK1wodIZmpiXHnDhMK6wr5OWXHCtmNhYgUKW0dWMMOsw4g%3D; __c=1746676855; __a=11158307.1746673487.1746673487.1746676855.12.2.3.12",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}


def download(page,position):
    url_tem = f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page={page}&pageSize=15&city=&position={position}'
    rep_tem = requests.get(url=url_tem,headers=headers)
    data_tem = rep_tem.json()['zpData']['jobList']

    # 将数据写入csv文件中
    # 打开文件
    with open("数据/data_boss_test.csv",mode='a',encoding='utf-8',newline='') as f_tem:
        csv_write_tem = csv.writer(f_tem)
        # 读入数据
        for item_tem in data_tem:
            csv_write_tem.writerow(item_tem.values())

    rep_tem.close()



if __name__ == '__main__':
    url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page=1&pageSize=15&city=101120200&position=100101&expectInfo=&query=&multiSubway=&multiBusinessDistrict=&jobType=&salary=&experience=&degree=&industry=&scale=&stage=&scene=1&_=1746677005986"
    rep = requests.get(url=url,headers=headers)
    print(rep.text)
    dic = rep.json()
    # data = dic['zpData']['jobList']
    # # 将数据标头写入csv文件中
    # # 打开文件
    # with open("数据/data_boss_test.csv",mode='w',encoding='utf-8',newline='') as f:
    #     csv_write = csv.writer(f)
    #     csv_write.writerow(data[0].keys())
    #
    # rep.close()
    #
    # # 读取职位id，逐个请求，并写入数据
    # f_position = pd.read_csv("数据/position.scv",header=0)
    # for item in f_position['code']:
    #     for page in range(1,11):
    #         download(page=page,position=item)
    #         break
    #         sleep(1)
    #     break


    print('over!!!')