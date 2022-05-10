from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("train.csv.bz2", "rb").read())[:10]

id,target
1,0
2,0
3,0
4,0
7,0
9,1
10,0
11,0
12,0
13,0

r = open('train.csv.bz2').read()
r = r[r.find('\n')+1:] # cut first line

len(r)
# 151436654
open("train.csv", "wb").write(BZ2Decompressor().decompress(r))

s = open("train.csv", "r")
s
# &lt;_io.TextIOWrapper name='train.csv' mode='r' encoding='UTF-8'&gt;
s.readlines()
</code>

