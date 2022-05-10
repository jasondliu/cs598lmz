from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, x: b''

def read_mnist(dataset="training", path="."):
    """
    Python function for importing the MNIST data set.  It returns an iterator
    of 2-tuples with the first element being the label and the second element
    being a numpy.uint8 2D array of pixel data for the given image.
    """

    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte.gz')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte.gz')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte.gz')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte.gz')
    else:
        raise ValueError, "dataset must be 'testing' or 'training
