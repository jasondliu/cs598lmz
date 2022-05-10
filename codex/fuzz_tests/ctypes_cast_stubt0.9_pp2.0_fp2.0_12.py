import ctypes
ctypes.cast(array, ctypes.py_object).contents = elements

# it doesn' test if the array is mature...
```
"""

# Inspired from :
# https://github.com/ActivisionGameScience/vectorclass/blob/master/vec4double.h
# https://github.com/ActivisionGameScience/vectorclass/blob/master/vec4float.h


import ctypes

def ndpointers(*typecodes):
    """Create a ndpointer type for each type code."""
    return tuple(np.ctypeslib.ndpointer(typecode, flags='C_CONTIGUOUS')
                 for typecode in typecodes)

# see https://github.com/ActivisionGameScience/vectorclass/blob/master/vec4float.h
float32_ctypes = [
    np.dtype(np.float32),
    np.dtype(np.float32).newbyteorder('<'),
    np.dtype(np.float32).newbyteorder('>'),
    np.dtype(np.float32).newbyteorder('='
