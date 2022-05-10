import lzma
lzma.LZMAFile(open('/home/ubuntu/workspace/tensorflow/tensorflow/contrib/learn/python/learn/datasets/mnist.py', 'rb'))

import gzip
with gzip.open('/home/ubuntu/workspace/tensorflow/tensorflow/contrib/learn/python/learn/datasets/mnist.py', 'rb') as f:
    file_content = f.read()

import bz2
with bz2.BZ2File('/home/ubuntu/workspace/tensorflow/tensorflow/contrib/learn/python/learn/datasets/mnist.py', 'rb') as f:
    file_content = f.read()

import lzma
with lzma.open('/home/ubuntu/workspace/tensorflow/tensorflow/contrib/learn/python/learn/datasets/mnist.py', 'rb') as f:
    file_content = f.read()
