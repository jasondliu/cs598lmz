import bz2
bz2Read = bz2.BZ2File('../tmp/buckets/search_trips_201711-201801.json.bz2', 'r')
bz2Read.readline().decode('utf-8')  # pass the header

#for x in bz2Read.readlines():
#    print(x.decode('utf-8'))

bz2Read.seek(0)
bz2Read.close()


# In[5]:


# efficient way of reading bz2 file using iterator
import bz2
bz2Read = bz2.BZ2File('../tmp/buckets/search_trips_201711-201801.json.bz2', 'r')
bz2Read.readline().decode('utf-8')
for line in bz2Read:
    print(line.decode('utf-8'))
bz2Read.close()


# ### Notes on reading JSON files
# 
# - you can use the standard `json` module to read the files
# - you may get an error
