import lzma
lzma.LZMAFile

# Import the data
with gzip.open('data/train-images-idx3-ubyte.gz', 'rb') as f:
    train_images = f.read()

with gzip.open('data/train-labels-idx1-ubyte.gz', 'rb') as f:
    train_labels = f.read()
    
with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
    test_images = f.read()

with gzip.open('data/t10k-labels-idx1-ubyte.gz', 'rb') as f:
    test_labels = f.read()

# Convert the data into numpy arrays
train_images = ~np.array(list(train_images[16:])).reshape(60000, 28, 28).astype(np.uint8) / 255.0
train_labels =  np.array(list(train_labels[ 8:])).ast
