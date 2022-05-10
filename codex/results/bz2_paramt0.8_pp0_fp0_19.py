from bz2 import BZ2Decompressor
BZ2Decompressor.decompress(bz2.open(raw_data_file).read())



def open_file(path):
    input = gzip.open(path, "rb")
    s = input.read()
    input.close()
    return s

file = open_file("pages.xml.bz2")
os.mkdir("wikiextractor-master")
p = os.getcwd()+"/wikiextractor-master"

os.chdir(p)

with open('test.xml', 'wb') as f:
    f.write(file)

f.close()

os.chdir("..")

print os.getcwd()


# In[39]:


import wikipedia as wiki

wiki.set_lang("ru")
wiki.search("Вероятностный алгоритм")[:5]


# In[40]:


wikipedia_page = wiki.page("Вероятностный
