from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.decompress(data))

# In[ ]:

# Get it from This link

# http://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2

# How to use

# python bz_file_reader.py jawiki-latest-pages-articles.xml.bz2


# In[2]:

import bz2
import json
import re

filepath = 'jawiki-country.json.gz'

def uk_reader():
    
    with bz2.open(filepath, 'rt') as g:
        for line in g:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']

    return value

# 正規表現のコンパイル
pattern = re.compile(r'''
    ^\{\{基礎情報.*?
