import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

view[0] = 42
view
# view[0] == 42

# ### `io.BytesIO`

# In[ ]:


import io

f = io.BytesIO(b'hello world')
f.read()
# b'hello world'

f
# <_io.BytesIO at 0x7f7c3db15a20>

f.tell()
# 11

f.seek(0)
f.read()
# b'hello world'

# ### `io.TextIOBase`
# 
# - `io.TextIOWrapper`
# - `io.StringIO`

# ### `io.StringIO`

# In[ ]:


import io

f = io.StringIO('hello world')
f.read()
# 'hello world'

f.write('hello')
f.write(' world')
f.seek(0)
f.read()
# 'hello world'

f.getvalue()
# 'hello world'

# ### `io.TextIOWrapper
