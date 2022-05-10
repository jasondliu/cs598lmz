import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
def make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)

df.style.format({'A': make_clickable})



# In[ ]:


df = pd.read_csv("C:/Users/Rez/Documents/GitHub/Python/Data/url.csv", encoding = 'utf-8')
df.head()


# In[ ]:


df.to_csv("C:/Users/Rez/Documents/GitHub/Python/Data/url1.csv", index=False, encoding='utf-8-sig')


# In[11]:


df.head()


# In[12]:


df = pd.read_csv("C:/Users/Rez/Documents/GitHub/Python/Data/url1.csv", encoding = 'utf-8')
df.
