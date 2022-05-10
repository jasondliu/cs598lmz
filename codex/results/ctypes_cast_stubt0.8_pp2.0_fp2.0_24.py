import ctypes
ctypes.cast(None, ctypes.py_object)


# In[9]:


#!/usr/bin/python

import ctypes

BASE_URL = 'http://192.168.56.101:8181/onos/v1'
USERNAME = 'onos'
PASSWORD = 'rocks'

lib = ctypes.cdll.LoadLibrary('./test.so')
lib.set_base_url(BASE_URL)
lib.set_username(USERNAME)
lib.set_password(PASSWORD)

print lib.test_c
