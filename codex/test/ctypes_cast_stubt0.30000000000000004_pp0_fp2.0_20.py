import ctypes
ctypes.cast(0, ctypes.py_object)

import sys
sys.getrefcount(None)

import gc
gc.collect()

# The following code is used to hide the 'magic' numbers in this program
# If you are just trying to get this to work on your machine, you can
# ignore this section.

import os.path

def add_modules_to_sys_path(path):
    """
    Utility method to add the given path to the python path
    """
    import sys
    path = os.path.abspath(path)
    if path not in sys.path:
        sys.path.insert(1, path)

add_modules_to_sys_path('..')

