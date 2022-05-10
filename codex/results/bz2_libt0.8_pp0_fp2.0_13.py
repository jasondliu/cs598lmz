import bz2
bz2.BZ2File('python-2.7.13.tar.bz2').read()[:100]

# %%
import bz2
f = bz2.open('python-3.6.3.tar.bz2', mode='wt')
f.write('对对对')
f.close()

# %%
import bz2
f = bz2.open('python-3.6.3.tar.bz2', mode='rt')
for line in f:
    print(line)
f.close()

# %%
import urllib.request
urllib.request.urlretrieve('https://www.python.org/ftp/python/3.6.3/python-3.6.3.tar.bz2', 'python-3.6.3.tar.bz2')

# %%
import tarfile
tar = tarfile.open('python-3.6.3.tar.bz2')
tar.extractall()
tar.close()

# %%
import os
os.list
