import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


# In[2]:


# Import data
df = pd.read_csv('data/data.csv', encoding = 'utf8')
df.head()


# In[3]:


# Create a list of stopwords
stopwords = stopwords.words('english')

# Create a function to remove stopwords
def remove_stopwords(text):
    try:
        text = text.split()
    except:
        return text
    text = [word for word in text if word not in stopwords]
    return ' '.join(text)

# Remove stopwords from text
df['text'] = df['text'].apply(remove_stopwords)
df.head()


# In[4]:


# Tokenize text
df['text'] = df['text'].apply(lambda x: x.split())
df.head()


# In[5]:


# Create a function to stem words
def stem_words(text):
    stemmer
