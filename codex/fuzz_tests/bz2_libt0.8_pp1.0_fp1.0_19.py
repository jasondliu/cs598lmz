import bz2
bz2.decompress(open('/home/ubuntu/workspace/tensorflow/mnist/t10k-images-idx3-ubyte.bz2', 'rb').read())

# install tensorflow-gpu version (which has gpu support)
!pip uninstall tensorflow -y
!pip uninstall keras -y
!pip install tensorflow-gpu
!pip install keras

import keras

# test that keras is setup correctly:
keras.backend.backend()
keras.backend.image_data_format()

# how does the memory use change over time?
!nvidia-smi

# memory usage is looking good, run the model...
!/home/ubuntu/anaconda3/bin/python3.6 /home/ubuntu/workspace/tensorflow/mnist/mnist_cnn.py

# or run the model with different batch sizes
!nvidia-smi
!/home/ubuntu/anaconda3/bin/python3.6 /home/ubuntu/workspace/tensorflow/
