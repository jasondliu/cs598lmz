import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

import gzip
with gzip.open('./data/test.txt.gz', 'rb') as fin:
    print(fin.read().decode('utf-8'))

# %%
import re
import requests

def crawl(url):
    response = requests.get(url)
    return response

url = 'https://movie.douban.com/'
response = crawl(url)
title = re.findall('<title>(.*?)</title>',response.text,re.S)[0]
print(title)

# %%
title = re.findall('<title>.*?</title>',response.text,re.S)[0]
print(title)

#
