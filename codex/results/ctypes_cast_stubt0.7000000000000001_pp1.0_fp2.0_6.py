import ctypes
ctypes.cast(1, ctypes.py_object)

s = 'hello'
s = s.encode()
s


# In[6]:


s = '안녕, 파이썬'
print(s)
b = s.encode()
print(b)
print(b.decode())


# In[7]:


bytes_val = b'ABC'
list_val = [b'A', b'B', b'C']
print(bytes_val)
print(list_val)


# In[8]:


print(bytes_val[0])
print(list_val[1])


# In[9]:


# bytes_val[0] = ord('D')

print(bytes_val)
print(list_val)


# In[10]:


import array

arr = array.array('b', [ord('A'), ord('B'), ord('C')])
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])



