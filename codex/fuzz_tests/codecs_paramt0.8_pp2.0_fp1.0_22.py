import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

# load the data
df = pd.read_csv(r'C:\Users\krish\Desktop\Machine learning\Yelp\yelp_review.csv',parse_dates=[3],encoding='utf-8')

# print basic info of dataframe
print('Dataset shape:',df.shape)

# print first 5 rows
df.head()

# print basic stats of dataframe
df.info()


# In[34]:


# creating a new column "text length" which is the number of words in the text column
df['text length'] = df['text'].apply(len)

# creating a dataframe with only 1 star and 5 star reviews
df_1_5 = df[(df.stars==1) | (df.stars==5)]

# X will be the 'text' column of df_1_5
X = df_1_5['text']

# y will be the 'stars' column of df_1_5
y = df_
