import bz2
bz2.decompress(f.read())

# In[ ]:


import gzip
gzip.open('file.gz', 'rt').read()

# In[ ]:


import lzma
lzma.open('file.xz').read()

# In[ ]:


import zipfile
zipfile.ZipFile('file.zip').read('some.dat')

# In[ ]:


import tarfile
t = tarfile.open('file.tar.gz')
t.extractall()
t.getmember('some.dat')

# In[ ]:


import pathlib
p = pathlib.Path('.')
p.iterdir()

# In[ ]:


import glob
glob.glob('*.py')

# In[ ]:


import shutil
shutil.copy('file.txt', 'file.txt.bak')
shutil.move('file.txt.bak', 'backup/')

# In[ ]:


import tempfile
temp = tempfile.TemporaryFile()

