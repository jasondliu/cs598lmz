import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    with open('res/jawiki-country.json.bz2') as f:
        for line in decompressor.decompress(f.read()).splitlines():
            article = json.loads(line)
            pprint.pprint(article)
            print('---- 間隔行 ----')
            break

# 処理速度の計測
import os,time
temp_fan = 'temp.txt'
start = time.time()
# ファイルの一行ずつ読み込む
with open(temp_fan,mode='r') as file:
    for line in file:
        pass
print(time.time() -start)
# ファイルを全部一度に読み込む
with open(temp_fan,mode='r') as file:
    contents = file.read()
print(time.time() -start)
os
