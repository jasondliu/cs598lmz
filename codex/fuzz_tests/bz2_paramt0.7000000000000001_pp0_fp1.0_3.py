from bz2 import BZ2Decompressor
BZ2Decompressor()

import urllib.request
import numpy as np

def get_file_from_url(url, file_name):
    response = urllib.request.urlopen(url)
    with open(file_name, 'wb') as f:
        f.write(response.read())

def get_mnist(directory):
    get_file_from_url(
        "http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
        os.path.join(directory, "train-images-idx3-ubyte.gz")
    )
    get_file_from_url(
        "http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
        os.path.join(directory, "train-labels-idx1-ubyte.gz")
    )
    get_file_from_url(
        "http://yann.lecun.com/exdb/mn
