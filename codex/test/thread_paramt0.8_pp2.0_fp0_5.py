import sys, threading
threading.Thread(target=lambda:sys.stdout.write('.')).start()

# In[1]:
import sys
sys.path.append('./models/research')
sys.path.append('./models/research/slim')
print(sys.path)

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

from nets import nets_factory
import numpy as np
import tensorflow as tf
import tensorflow.contrib.slim as slim
from datetime import datetime
import os
import time
import matplotlib.pyplot as plt
from preprocessing import preprocessing_factory
from tensorflow.contrib import slim as slim

# In[2]:

tf.logging.set_verbosity(tf.logging.INFO)

# In[3]:

# Basic model parameters.

model_name = 'inception_v4'

# In[4]:

batch_size = 24

# In[5]:

preprocessing_name = None

# In[6]:

image_size
