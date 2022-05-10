import ctypes
ctypes.cast(None, ctypes.py_object)

import sys
sys.modules['_ctypes'] = sys.modules['ctypes']
del sys

del ctypes
</code>
This prevents the import of <code>ctypes</code> (and the <code>_ctypes</code> module that it imports) but still allows other modules to import <code>_ctypes</code> without any issues. The code for <code>ctypes</code> was adapted from this answer.

