from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# In[ ]:


import lzma
with lzma.open("../input/test.csv.xz") as f:
    file_content = f.read()


# In[ ]:


# Read 5 rows
import csv
from io import StringIO
reader = csv.reader(StringIO(file_content.decode('utf-8')))
for line in reader:
    print(line)


# In[ ]:


# Read 5 rows
import pandas as pd
pd.read_csv(StringIO(file_content.decode('utf-8')), nrows=5)

# In[ ]:


import zipfile
with zipfile.ZipFile("../input/train.csv.zip") as zf:
    with zf.
