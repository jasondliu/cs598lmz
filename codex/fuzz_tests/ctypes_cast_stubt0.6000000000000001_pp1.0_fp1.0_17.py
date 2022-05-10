import ctypes
ctypes.cast(NULL_HANDLE, ctypes.c_void_p).value

NULL_HANDLE = ctypes.c_void_p(-1)
NULL_HANDLE.value

# %% [markdown]
# ## NULL_HANDLE is a valid pointer

# %%
ctypes.cast(NULL_HANDLE, ctypes.c_void_p)

# %% [markdown]
# ## And can be used with ctypes

# %%
ctypes.cast(NULL_HANDLE, ctypes.c_void_p).value

# %% [markdown]
# ## NULL_HANDLE is not a valid pointer

# %%
ctypes.cast(NULL_HANDLE, ctypes.POINTER(ctypes.c_uint32))

# %% [markdown]
# ## NULL_HANDLE is a valid pointer

# %%
ctypes.cast(NULL_HANDLE, ctypes.POINTER(ctypes.c_uint32)).contents

# %% [markdown]
# ## NULL_HANDLE is a valid pointer
