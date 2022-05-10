import ctypes
ctypes.cast(4, ctypes.c_int64)

# %%
import numpy as np
np.int64(4)

# %%
np.int64(4) == 4

# %%
np.int64(4) is 4

# %%
np.int64(4) is int(4)

# %%
np.float64(np.int64(4))

# %%
np.float64(np.int64(4)) is np.float64(4)

# %%
np.int64(4) == np.float64(4)

# %%
(np.int64(4), np.float64(4))

# %%
np.complex128(4)

# %%
np.complex128(4) == np.complex128(4.0)

# %%
np.complex128(4) == np.complex128(4.)

# %%
np.complex128(4) == np.complex128(4.000001)

# %%
4.000000000001 == 4.0

# %%
np.complex128(
