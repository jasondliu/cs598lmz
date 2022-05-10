import _struct

import numpy as np

def read_data(path):
    with open(path, 'rb') as f:
        zero, data_type, dims = _struct.unpack('>HBB', f.read(4))
        shape = tuple(dims)
        return np.fromstring(f.read(), dtype=np.uint8).reshape(shape)

def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte'
                               % kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = _struct.unpack('>II',
                                  lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint
