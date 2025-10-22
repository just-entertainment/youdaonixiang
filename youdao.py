# import requests
import curl_cffi
from  curl_cffi import requests
import execjs
from  base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

file=open('youdao.js', 'r', encoding='UTF-8').read()
ctx=execjs.compile(file)
list=ctx.call('k')
sign=list['sign']
mysticTime=list['mysticTime']
headers= {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "connection": "keep-alive",
    "content-length": "339",
    "content-type": "application/x-www-form-urlencoded",
    "cookie": "OUTFOX_SEARCH_USER_ID=-442871225@240e:341:4d15:7d00:e8cb:5d19:c87b:c54d; OUTFOX_SEARCH_USER_ID_NCOO=315751709.87457407; NTES_YD_PASSPORT=dQ8ELByk25vFB_Pdtgk3IeyaVP870doIzaprBOXquyJu.6Js.4TFkUpv6h7riHzoA3Scewf8LwHq7dr4yK4OTaCNP4Uzqy58_C4pOI3GnusNL.y6enCl1Q_P1FGhrNMmEOQK6tXFX8T0AgRWIDnAlg3TPz2yFpmdFS_uTRnDSoGD8lHlQv2BcgIPcvKtxsoT7DKJJLtmo5LKZ.GJkLUHnZaTUsMh1SjQS; P_INFO=15631128911|1760969380|1|dict_logon|00&99|null&null&null#heb&130500#10#0|&0||15631128911; DICT_PERS=v2|urs-phone-web||DICT||web||-1||1760969381643||240e:341:4d15:7d00:e8cb:5d19:c87b:c54d||urs-phoneyd.2b93ddf376e040b08@163.com||qLkMqF6LgK0PZ64kEhHwBRUYOflmhLQuRYMnHz5OLQZ0Ty6LgZ6Lzm0kMnLO5P4pS0qFnLPFRLzMR6ShLTynHPZ0; DICT_UT=urs-phoneyd.2b93ddf376e040b08@163.com; DICT_SESS=v2|scsq97LYs0Q4k4PzhfQLRU5h4qKhLQL0qu0LTB6MOGRl5RfPBkfwBROEhLOGk4eF06z64JS0fTL0YMnHJuO4km0lAOMUGOLll0; DICT_LOGIN=3||1761100771925; _uetsid=431e6620adbe11f08feb6967473b0937; _uetvid=431e8780adbe11f085d58b06111a2495; _uetmsclkid=_ueta62a706d971719273e621895d4f7063a; DICT_DOCTRANS_SESSION_ID=MDJiYWI3NzAtYTliOS00MWNlLThmMmEtMzA3YTQ0ZmM5NTEx",
    "host": "dict.youdao.com",
    "origin": "https://fanyi.youdao.com",
    "pragma": "no-cache",
    "referer": "https://fanyi.youdao.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}
ainput=input()
params= {
    "i": ainput,
    "from": "zh-CHS",
    "to": "en",
    "useTerm": "false",
    "domain": "0",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": str(sign),
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": str(mysticTime),
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg"
}
url='https://dict.youdao.com/webtranslate'
res=requests.post(url=url,headers=headers,data=params)

data=res.text
print(data)
res=b64decode(data.replace('-','+').replace('_','/').encode())

key=bytes([8, 20, 157, 167, 60, 89, 206, 98, 85, 91, 1, 233, 47, 52, 232, 56])
iv=bytes([210, 187, 27, 253, 232, 59, 56, 195, 68, 54, 99, 87, 183, 156, 174, 28])
a=AES.new(key,AES.MODE_CBC,iv)
res=a.decrypt(res)
print(unpad(res,16).decode())



