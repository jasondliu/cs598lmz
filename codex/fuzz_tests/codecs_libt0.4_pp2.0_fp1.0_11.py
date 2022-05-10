import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


# In[2]:


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',                             
                             db='capstone',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# In[3]:


# Function to get the most common words in a list of tweets
def get_most_common(tweets, num_words):
    word_list = []
    for tweet in tweets:
        for word in tweet.split():
            word_list.append(word)
    counter = Counter(word_list)
    return counter.most_common(num_words)


# In[4]:


# Function to get the most common words in a list of tweets
def get_most_common_hashtags(tweets, num_words):
    word_list = []
    for tweet
