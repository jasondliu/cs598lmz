from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# data = open('./data/mushroom.csv.lzma', 'rb').read()
# decompressed_data=bz2.decompress(data)
# print(decompressed_data)


# In[ ]:


# import lzma
# with lzma.open('./data/mushroom.csv.lzma') as f:
#     file_content = f.read()
#     file_content


# In[ ]:


# import lzma
# with lzma.open('./data/mushroom.csv.lzma') as f:
#     file_content = f.read()
#     for line in file_content:
#         print(line)


# In[ ]:


# import lzma
# with lzma.open('./data/mushroom.csv.lzma') as f:
#     file_content = f.readlines()
#     file_content


# In[ ]
