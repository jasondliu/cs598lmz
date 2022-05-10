import bz2
# Test BZ2Decompressor

fd = open('enwiki-latest-pages-articles.xml.bz2', 'rb')
d = bz2.BZ2Decompressor()
n = d.readline()
print(n.decode('utf8'))
n = d.readline()
print(n.decode('utf8'))


# In[ ]:
