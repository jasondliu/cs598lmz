import bz2
bz2_file = bz2.BZ2File('./data/titles-enwiki-latest.xml.bz2')

for line in bz2_file:
    title = line.decode('utf-8').split('\t')[1]
    print(title)
    break

#%%
from bz2 import BZ2File
bz2_file = BZ2File('./data/titles-enwiki-latest.xml.bz2')

for line in bz2_file:
    title = line.decode('utf-8').split('\t')[1]
    print(title)
    break

#%%
from bz2 import BZ2File
bz2_file = BZ2File('./data/titles-enwiki-latest.xml.bz2')

for line in bz2_file:
    title = line.decode('utf-8').split('\t')[1]
    print(title)
    break

#%%
# バイナリデータ
