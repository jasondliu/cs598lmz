from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('data/enwiki-latest-pages-articles.xml.bz2', 'rb').read())

#%%
import bz2
with bz2.open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    file_content = f.read()

#%%
import bz2
with bz2.open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    for line in f:
        print(line)

#%%
import bz2
with bz2.open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    for line in f:
        print(line.decode())

#%%
import bz2
with bz2.open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    for line in f:
        print(line.decode().strip())

#%%
import bz2

