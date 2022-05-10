import codecs
codecs.register_error('ignore', codecs.lookup_error('mbcs'))

#%%
path = "C:\\Users\\Qiushi\\Desktop\\Projects\\ML\\Dataset\\CNSMovie_Review\\"
reviews_train = []
for line in open(path + 'movie_data/full_train.txt', 'r'):
    reviews_train.append(line.strip())
    
reviews_test = []
for line in open(path + 'movie_data/full_test.txt', 'r'):
    reviews_test.append(line.strip())
    
#%% [markdown]
# #### 2.1 数据的探索性分析

#%%
REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_reviews(reviews):
    reviews =
