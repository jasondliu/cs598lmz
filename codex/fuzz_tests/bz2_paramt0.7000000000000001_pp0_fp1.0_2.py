from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("data/train.ft.txt.bz2", 'rb').read())

#%%
import bz2
with open('data/train.ft.txt.bz2', 'rb') as file:
    file_content = bz2.decompress(file.read())
    file_content = file_content.decode("utf-8")

#%%
