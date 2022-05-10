from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(x)

# In[ ]:

import gzip
with gzip.open('data/t10k-images-idx3-ubyte.gz','rb') as f:
    file_content = f.read()

# ### Read MNIST

# In[ ]:

#Look at this example: http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py
with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    labels = np.frombuffer(f.read(), dtype=np.uint8, offset=8)

# In[ ]:

with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
    data = np.frombuffer(f.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)

# In[ ]:

get_ipython().magic('matplotlib inline')
