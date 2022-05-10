import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
sys.modules['_ctypes'] = None
sys.modules['ctypes'] = None

import gc
gc.collect()

import os
os.system('pip install --upgrade pip')

import sys
sys.modules['_ctypes'] = None
sys.modules['ctypes'] = None

import gc
gc.collect()

import os
os.system('pip install --upgrade gensim')

import sys
sys.modules['_ctypes'] = None
sys.modules['ctypes'] = None

import gc
gc.collect()

import os
os.system('pip install --upgrade nltk')

import sys
sys.modules['_ctypes'] = None
sys.modules['ctypes'] = None

import gc
gc.collect()

import os
os.system('pip install --upgrade lda')

import sys
sys.modules['_ctypes'] = None
sys.modules['ctypes'] = None

import gc
