import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

#%%
#import warnings
#warnings.filterwarnings('ignore')

#%%
# read data
df = pd.read_csv('data/data.csv',index_col=0)

#%% [markdown]
# ## Explore data
#%% [markdown]
# ### Check data type

#%%
df.info()

#%% [markdown]
# ### Check missing values

#%%
df.isnull().sum()

#%% [markdown]
# ### Check correlation

#%%
corr = df[['price','bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition','grade','sqft_above','sqft_basement','yr_built','yr_renovated','zipcode','lat','long','sqft_living15','sqft_lot15']].corr()
corr

#%% [markdown]
# ### Check data distribution

#%%
