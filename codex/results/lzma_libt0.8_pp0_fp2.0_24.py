import lzma
lzma.open

# https://bitbucket.org/pypy/pypy/src/f6cad69c8b3e3c3f64973825b2d6dc941f1b6a66/pypy/module/lzma/test/test_lzma.py?fileviewer=file-view-default#test_lzma.py-834
# https://pbpython.com/compression-in-pandas.html

# In[ ]:


# EM -  copy pasted from above and I added
#       .dtypes
#       .nunique()
#       .isnull().sum()
# can remove later

# types
print('dtypes')
print(df.dtypes)

# unique values per column
print('nunique')
for col in df.columns:
    print(df[col].nunique())

# nulls per column
print('isnull().sum()')
print(df.isnull().sum())

# In[ ]:


# EM clear out unused objects
