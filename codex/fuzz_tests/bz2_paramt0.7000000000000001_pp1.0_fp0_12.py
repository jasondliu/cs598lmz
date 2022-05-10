from bz2 import BZ2Decompressor
BZ2Decompressor


# In[ ]:


# Get the dictionary of dataframes.
df_dict = pd.read_pickle('../data/processed/dataframe_dict_new.pkl')


# In[ ]:


# Get the set of all possible categories.
all_categories = set()
for key in df_dict.keys():
    all_categories = all_categories.union(df_dict[key].category.unique())
all_categories = list(all_categories)


# In[ ]:


stopwords = set(stopwords.words('english'))


# In[ ]:


# Define the function to clean up text.
def clean_up(text):
    '''
    Given text, cleans it up, returning only words.
    '''
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text)
    text = text.split()
    text = [w for w in text if not w in stopwords]
    text = " ".join(
