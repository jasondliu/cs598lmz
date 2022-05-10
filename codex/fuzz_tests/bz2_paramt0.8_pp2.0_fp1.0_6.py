from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)


# In[31]:

f = open('c:/Users/Admin/Downloads/python.txt', 'rb')
data = f.read()
f.close()

for line in data.split('\r\n'):
    print line
