import codecs
codecs.open("/Users/raghuram.b/Desktop/mayweather/mayweather.txt", 'r', 'utf-8')


# In[113]:


with codecs.open("/Users/raghuram.b/Desktop/mayweather/mayweather.txt", 'r', 'utf-8') as f:
    for line in f:
        print(line)


# In[114]:


# Read the file in binary mode
f = open("/Users/raghuram.b/Desktop/mayweather/mayweather.txt", "rb")


# In[115]:


f.read()


# In[116]:


# Read the file in text mode
f = open("/Users/raghuram.b/Desktop/mayweather/mayweather.txt", "r")


# In[117]:


f.read()


# In[118]:


# Write the file in binary mode 
f = open("/Users/raghuram.b/Desktop/mayweather/mayweather.txt", "wb")
f.write(b
