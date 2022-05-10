from lzma import LZMADecompressor
LZMADecompressor().decompress(open('C:\\Users\\Administrator\\Desktop\\python\\fin_data\\sz\\sz.000001.xz', 'rb').read())

import pandas as pd
df = pd.read_json("C:\\Users\\Administrator\\Desktop\\python\\fin_data\\sz\\sz.000001.json")
df.head(3)

df = pd.read_json("C:\\Users\\Administrator\\Desktop\\python\\fin_data\\sz\\sz.000001.json",orient='split')
df.head(3)

df = pd.read_json("C:\\Users\\Administrator\\Desktop\\python\\fin_data\\sz\\sz.000001.json",orient='index')
df.head(3)

df = pd.read_json("C:\\Users\\Administrator\\Desktop\\python\\fin_data\\sz\\sz.000001.json",orient='columns')
df.head(3)


df = pd.read_json("C:\\Users\\
