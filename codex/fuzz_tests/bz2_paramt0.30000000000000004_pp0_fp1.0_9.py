from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# 对于文件，可以使用bz2.open()，它返回一个BZ2File对象，和普通的文件对象一样，可以使用read()、write()、close()等方法
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)
with bz2.open('somefile.bz2', 'rt') as f:
    print(f.read())

# In[ ]:


# 如果你想控制压缩级别，可以传递一个可选的级别参数
with bz2.open('somefile.bz2', 'wt', compress
