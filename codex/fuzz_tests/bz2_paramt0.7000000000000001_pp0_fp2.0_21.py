from bz2 import BZ2Decompressor
BZ2Decompressor(max_wbits=24)

# Downloading the data
import os
data_folder = os.path.expanduser('~/data/mnist')
if not os.path.exists(data_folder):
    os.mkdir(data_folder)

# Downloading the data
import urllib.request
url = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
local_file = os.path.join(data_folder, 'train-images-idx3-ubyte.gz')
urllib.request.urlretrieve(url, local_file)

# Loading the data
with gzip.open(local_file, 'rb') as f:
    train_images = np.frombuffer(f.read(), np.uint8, offset=16)
train_images = train_images.reshape(-1, 784)

# Downloading the data
url = 'http://yann.lecun.com/exdb/mnist/train-labels-
