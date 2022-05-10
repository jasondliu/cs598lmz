import bz2
# Test BZ2Decompressor
with open("data/docs_html.bz2", 'rb') as f:
    with bz2.BZ2Decompressor() as d:
        for line in iter(lambda: d.decompress(f.read(100)), b''):
            print(line.decode(), end='', flush=True)

# That's it!

# ### Warning! The context manager doesn't close the underlying file!

# In[16]:


with open("data/docs_html.bz2", 'rb') as f:
    with bz2.BZ2Decompressor() as d:
        for line in iter(lambda: d.decompress(f.read(100)), b''):
            print(line.decode(), end='', flush=True)
f.close()

# ## Regex

# ### Python's Regex (re) module
# * `re` module includes:
#     * functions for regex search and substitution
#         * substrings starting at position `m.start()`, ending just before `m.end()`
#     * classes
