import ctypes
ctypes.cast(1, ctypes.py_object)

#Sets

# In[2]:

x = set()
x


# In[3]:

x.add(1)


# In[4]:

x


# In[5]:

x.add(2)


# In[6]:

x


# In[7]:

l = [1,1,2,2,3,4,5,6,1,1]


# In[8]:

set(l)


#Booleans

# In[9]:

a = True


# In[10]:

1 > 2


# In[11]:

11 > 2


# In[12]:

b = None


# In[13]:

b


#Files

# In[14]:

%%writefile myfile.txt
Hello this is a text file
this is the second line
this is the third line


# In[15]:

myfile = open('myfile.txt')


# In[16]:

p
