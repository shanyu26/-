"""
尝试使用异步协程requests爬取数据，但没绕过反爬机制，无法访问职位列表。
"""

import requests
import csv
import aiohttp
import aiofiles
import asyncio

headers = {
    "cookie":"ab_guid=67327eb2-a312-40e3-9c1a-5e94dbb52810; lastCity=100010000; wt2=DVYVYmcuz6zeesdpbVVFcO0hAS_TiZQlNTCUCBbFH25TOBghszwoShvLmLo-AqIxux3wxmboYxICO_PtaBBfxTA~~; wbg=0; zp_at=K2c2qthVSK-WkpCUQFXfMmCtlvTczN6304ebC8RL-Vo~; __zp_seo_uuid__=a92fe387-856e-457c-91d9-21628e9fa2d0; __zp_stoken__=7d89fQTvDpsK%2BwpzDgkYtChcNCA9FLEY7KihEQS9COUBBOzw7QkE7RBk8MWTEuiY2XsOMRTkuQTtDOTs%2FOzxEHkFHxLrCvjpAMULEvyQsZMOLCk0SYQ%2FCucK8N8KgwrwKDzopwoTCuDxGRDtewrlGw4YLwrs8wrwMwr4%2Bw4ZGPDs%2BNkIWEQgJQjxIT1kUTmROY15SCVdVTy47RTpBw7DDrMO%2BMEMWERQWDBYRFBYMFRIXDBYMCw4MFhUSFxUPMzzCm8K8xK3FncOlVMSmxbTDlcK0xJ3CmsShwqzErMKgw4%2FCoMSpw73DkcK0xLTCpMSow7nDoMKuw7HDuMOXwp%2FDs1LDrVPDicKIw6bCusOdw4HDtsK%2Fw6bCsMO6wqbDmlXCtGPDqF3CoFjCrmrCtMKbwqXCscOHwp%2FCisKtwo5Vwq5lwo1uwpNswqLCrVDCtMK8w4DCnmdfw4JJWsK3Y8OEfsKHVl3CvH9fWsKFfmEROGLCiU3DjA%3D%3D; __g=-; __l=r=https%3A%2F%2Fcn.bing.com%2F&l=%2Fwww.zhipin.com%2F&s=1&g=&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1745757972,1746275669,1746282752; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1746282752; HMACCOUNT=8D9C662CDBA01E84; bst=V2R94lE-35015rVtRuyxsRKSi27DrRzCs~|R94lE-35015rVtRuyxsRKSi27DrVwi4~; __c=1746282752; __a=81689086.1742104377.1746275669.1746282752.33.5.3.33",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}


async def download(page,position):
    url = f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page={page}&pageSize=15&city=&position={position}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url,headers=headers) as rep:
            dic = await rep.json()

            data = dic['zpData']['jobList']

        # 将数据写入csv文件中
        # 打开文件
        async with aiofiles.open("data/data_boss_test.csv",mode='a',encoding='utf-8',newline='') as f:
            csv_write = csv.writer(f)

            # 读入数据
            for item in data:
                await csv_write.writerow(item.values())


async def main(number,city,position):
    url = f'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page=1&pageSize=15&city={city}&position={position}'
    rep = requests.get(url = url,headers=headers)
    dic = rep.json()
    data = dic['zpData']['jobList']

    # 将数据写入csv文件中
    # 打开文件
    with open("data/data_boss_test.csv", mode='w', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data[0].keys())
        # 读入数据
        for item in data:
            csv_write.writerow(item.values())

    rep.close()
    tasks = []
    for i in range(2,number):
        tasks.append(asyncio.create_task(download(page=i,city=city,position=position)))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main(3,100010000,100101))
    print('over!!!')