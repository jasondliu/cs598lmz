import bz2
bz2.BZ2File('../wiki/jawiki-country.json.bz2').read()

# JSONを読み込む
import json

# wikiのデータを取得
wiki_data = []
with bz2.BZ2File('../wiki/jawiki-country.json.bz2') as f:
    for line in f:
        json_data = json.loads(line)
        wiki_data.append(json_data)

# タイトルがイギリスになっているデータを抽出
for r in wiki_data:
    if r['title'] == 'イギリス':
        print(r['text'])

import re

# 基礎情報の取得
basic_info = re.search(r'基礎情報 国\n(.*?)\n\}\}',r['text'],re.DOTALL)
basic_info = basic_info
