import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


# In[2]:

source_folder=r'C:\Users\lzhang27\Documents\GitHub\Capstone\Twitter_Data'


# ## 1. Load the data base

# In[3]:

import_file=os.path.join(source_folder, 'tweet_data.csv')
tweet_data=pd.read_csv(import_file, encoding='utf-8', low_memory=False)


# In[4]:

tweet_data.head()


# ## 2. Remove the duplicates

# In[5]:

tweet_data.drop_duplicates(subset=['user_id', 'text', 'created_at'], inplace=True)


# In[6]:

tweet_data.info()


# In[7]:

#tweet_data.to_csv(import_file, sep=',', encoding='utf-8')


# ## 3
