import requests
headers = {
    "cookie":"lastCity=101120200; b-user-id=5f18687a-0cfe-4c11-ffc0-9dfbf43a7f1f; ab_guid=3cff27d9-9617-49a8-8845-c9a68add9bd9; __g=-; __l=l=%2Fwww.zhipin.com%2Fqingdao%2F%3Fka%3Dheader-home%26seoRefer%3Dindex&r=&g=&s=3&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1746673487,1746676856; HMACCOUNT=31384717267B9CB5; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1746676857; __zp_stoken__=b10dfPDjDmcK6wp7Cv0ExFAgMCxRBMzs4LhM2PCw2NT88OEQ7OTw4PBVDLF3Cvh4vY8OPwrrCukElOERCRDxCRDU1FTg4xL%2FDgzk1L1%2FCviczW8OKFx%2FCuGLDl8ODD8OIw4MGw5HCuwtXwrUuKsKAw4E6Q0M%2FY8K7Q8K9D8OCOsK1C8K2Q8OEQzs%2FQzRHDRIMBkc7TE5bDUVgU11bUQlGV0YlPzg4RMKLwp4qOwgQFAgRBQ0RBRQRCQUIERMLDxMKEQkFEQgsPMKhw4PDjsOjw4VTxJXFrMOGwrTFgsO0xKPCjsStw7jEoMKYxKbEg8OPwrXDqcK0w4XCkMOew4PDicK1w6TCtMO8wqbDtsKNw4rDgsOXTsOlwqTDmsKjwpnCrsOvZMOhw4fDvMKhwovCrMOtw4LCrcK7w7DCm8KWwrDCnE%2FDulzCn2bCj8OEwp7Cv8KbbVLDgsK4VsK2TsK1wodIZmpiXHnDhMK6wr5OWXHCtmNhYgUKW0dWMMOsw4g%3D; __c=1746676855; __a=11158307.1746673487.1746673487.1746676855.12.2.3.12",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
}

proxies = {
    "https":"http://116.208.202.139:23380"
}

url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?page=1&pageSize=15&city=101120200&position=100101&expectInfo=&query=&multiSubway=&multiBusinessDistrict=&jobType=&salary=&experience=&degree=&industry=&scale=&stage=&scene=1&_=1746677005986'
rep = requests.get(url="https://www.baidu.com/", headers=headers,proxies=proxies)
print(rep.text)
