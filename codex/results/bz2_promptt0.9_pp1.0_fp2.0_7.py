import bz2
# Test BZ2Decompressor
with open('chinese.pickle.bz2', 'rb') as f_in, open('chinese.pickle', 'wb') as f_out:
    decoder = bz2.BZ2Decompressor()
    for block in iter(lambda : f_in.read(1024), b''):
        f_out.write(decoder.decompress(block))

import pickle
data = pickle.load(f_out)
type(data)

import jieba
data

for line in data:
    line[1] = ' '.join(jieba.lcut(line[1]))
data

######save text to a file######
file = open("chinese_smart.txt","a")
for line in data:
    file.write(str(line[1]))
    file.write("\n")
file.close()
