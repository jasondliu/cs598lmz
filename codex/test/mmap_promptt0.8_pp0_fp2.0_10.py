import mmap
# Test mmap.mmap(f.fileno(), 0, flags=mmap.MAP_PRIVATE)

def display_file(n, fname):
    with open(fname, 'r') as f:
        lines = mmap.mmap(f.fileno(), 0, flags=mmap.MAP_PRIVATE)
        print('-' * 50)
        print(n)
        print('\n'.join(lines[:50]))


for n in range(0, 5):
    try:
        display_file(n, 'aux_data/%d.txt' % n)
    except Exception as err:
        print(err)
        break
 

# In[94]:


flist = ['aux_data/%d.txt' % n for n in range(0, 5)]

for n in range(0, 5):
    display_file(n, flist[n])


# In[95]:


files = [open(fname) for fname in flist]
files


# In[96]:


files[0].close()


