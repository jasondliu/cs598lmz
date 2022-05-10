from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# In[ ]:


# 从字符串中提取变量
import re
text = 'foo = 23 + 42 * 10'
m = re.search('(\d+) \+ (\d+) \* (\d+)', text)
m.group(0)
m.group(1)
m.group(2)
m.group(3)
m.groups()

# In[ ]:


# 字节字符串上的字符串操作
data = b'Hello World'
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello', b'Hello Cruel')

# In[ ]:


# 字节数组
data = bytearray(b'Hello World')
data[0:5]
data.startswith(b'Hello')
data.split()
data.replace(b'Hello
