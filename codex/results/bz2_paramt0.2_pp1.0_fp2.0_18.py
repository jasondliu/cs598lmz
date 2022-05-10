from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# In[ ]:


# Write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def file_lengthy(filename):
    try:
        f = open(filename)
        return len(f.readlines())
    except FileNotFoundError:
        return 0

# In[ ]:


# Write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def file_lengthy(filename):
    try:
        f = open(filename)
        return len(f.readlines())
    except FileNotFoundError:
        return 0

# In[ ]:


# Write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.

def file_lengthy(filename):
    try:
        f = open(filename)
        return len(f.readlines())
    except FileNotFoundError:
        return 0
