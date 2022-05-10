import codecs
codecs.open('/content/file.txt', 'rU', 'utf-8', 'strict', 100)
!wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz -O mnist/train-images-idx3-ubyte.gz
!wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz -O mnist/train-labels-idx1-ubyte.gz
!wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz -O mnist/t10k-images-idx3-ubyte.gz
!wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz -O mnist/t10k-labels-idx1-ubyte.gz

!zcat m
