import ctypes
ctypes.cast(rb_obj.data, ctypes.POINTER(ctypes.c_int32))

# %%
import numpy as np
np.ctypeslib.as_array(rb_obj.data, (rb_obj.lenght,))
# %%
import numpy as np

abjad_channels = []
for _ in range(8):
    abjad_channels.append(rb_obj.pop())

abjad_channels = np.asarray(abjad_channels, dtype=np.int32)

abjad_channels

# %%
abjad_channels.shape

# %%
np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='C')

# %%
import ctypes
import numpy as np

ctype = np.ctypeslib.ndpointer(dtype=np.int32, ndim=1, flags='C')
restype = ctypes.c_int
argtype = ctype

import IPython

lib = ctypes.CDLL('/home/
