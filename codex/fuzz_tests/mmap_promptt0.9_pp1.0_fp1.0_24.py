import mmap
# Test mmap.mmap(-1, 5 , prot=mmap.ACCESS_WRITE)


# In[123]:


acces_file=open(file_name,'r+',encoding='cp1251')
acces_maps=mmap.mmap(acces_file.fileno(),0,prot=mmap.PROT_READ)
c=acces_maps[14:15]
acces_maps.close()
acces_file.close()
print(c)


# In[124]:


if c!=None:
    if c == b'\xd0':
        print('pravda')


# In[125]:


print(mmap.PROT_READ)
print(mmap.ACCESS_COPY)


# In[127]:


c=None
if c==None:
    print('pravda')


# In[46]:


mmap.mmap.__init__()


# In[ ]:
