from bz2 import BZ2Decompressor
BZ2Decompressor = BZ2Decompressor()

def load_data(path):
    """
    Loads the dataset.
    """
    # Load the dataset
    f = gzip.open(path, 'rb')
    data = np.frombuffer(f.read(), np.uint8, offset=16)
    f.close()

    # Reshape the data
    data = data.reshape(-1, 1, 28, 28)

    # The inputs come as bytes, we convert them to float32 in range [0,1].
    # (Actually to range [0, 255/256], for compatibility to the version
    # provided at http://deeplearning.net/data/mnist/mnist.pkl.gz.)
    return data / np.float32(256)


def load_labels(path):
    """
    Loads the dataset.
    """
    # Load the dataset
    f = gzip.open(path, 'rb')
    data = np.frombuffer(f.read(), np.uint8, offset=8)
    f.close()

    # The
