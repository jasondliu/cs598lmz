import ctypes
ctypes.cast(1, ctypes.py_object)
ctypes.cast(1, ctypes.c_int)

import array
array.array('f', [1, 2, 3])
array.array('f', [1, 2, 3]).tolist()

import pprint
pprint.pprint(['spam', 'eggs', 'ham'])
pprint.pformat(['spam', 'eggs', 'ham'])

import time
time.asctime()
time.localtime()
time.gmtime()
time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
time.strptime('2008-09-29 12:15:27', '%Y-%m-%d %H:%M:%S')
time.mktime(time.strptime('2008-09-29 12:15:27', '%Y-%m-%d %H:%M
