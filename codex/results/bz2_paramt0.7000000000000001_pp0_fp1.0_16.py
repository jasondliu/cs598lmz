from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


print(time.ctime(os.path.getctime(file_name)))
print(time.ctime(os.path.getmtime(file_name)))
print(time.ctime(os.path.getatime(file_name)))

# In[ ]:


print(os.path.getsize(file_name))
print(os.path.splitext(file_name))

# In[ ]:


os.listdir(os.getcwd())

# In[ ]:


os.listdir(os.getcwd())

# In[ ]:


#os.mkdir("test")
#os.makedirs("test/test1/test2")

# In[ ]:


#os.rmdir("test")
#os.removedirs("test/test1/test2")

# In[ ]:


#os.rename("test.txt", "test2.txt")
#os.rename("test2.txt",
