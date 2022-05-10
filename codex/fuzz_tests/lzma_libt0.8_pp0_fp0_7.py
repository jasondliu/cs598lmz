import lzma
lzma.decompress(open("data/people_wiki.csv.lzma", "rb").read())

people = pd.read_csv(io.StringIO(lzma.decompress(open("data/people_wiki.csv.lzma", "rb").read()).decode("UTF-8")))

print(people.head())

# In[14]:


# people.head()

# In[15]:


# people.shape

# ### Exploring the dataset and checking out the text it contains
# 
# Let's take a look at the entry for Obama and see how it differs from the entry for the actor George Clooney.

# In[16]:


obama = people[people['name'] == 'Barack Obama']
obama

# In[17]:


clooney = people[people['name'] == 'George Clooney']
clooney

# In[18]:


obama['text']

# In[19]:


clooney['text']

# ## Word counts for Obama acticle

#
