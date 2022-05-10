import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()


# In[3]:


# Load the TensorBoard notebook extension
get_ipython().run_line_magic('load_ext', 'tensorboard')


# In[4]:


# Clear any logs from previous runs
get_ipython().system_raw('rm -rf ./logs')


# In[5]:


import tensorflow as tf
import datetime


# In[6]:


mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

