import ctypes
ctypes.cast(0, ctypes.py_object)

import os
os.environ["PYTHONPATH"] = ":".join((
    "/usr/local/lib/python2.7/dist-packages/",
    "/usr/lib/python2.7/dist-packages/",
    "/usr/lib/python2.7/",
))

