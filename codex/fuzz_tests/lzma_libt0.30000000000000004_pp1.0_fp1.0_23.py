import lzma
lzma.decompress(data)

# In[ ]:


# 字符串编码
# 使用encode()方法可以编码为指定的bytes
'ABC'.encode('ascii')
'中文'.encode('utf-8')

# In[ ]:


# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# In[ ]:


# 要计算str包
