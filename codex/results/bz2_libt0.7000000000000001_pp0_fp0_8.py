import bz2
bz2.BZ2File('train.ft.txt.bz2').readlines()

# In[40]:


import nltk
nltk.download()

# In[41]:


from nltk.stem import WordNetLemmatizer

# In[42]:


lemmatizer = WordNetLemmatizer()

# In[43]:


print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))
print(lemmatizer.lemmatize("best", pos="a"))
print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",'v'))

# In[44]:


import pandas as p
