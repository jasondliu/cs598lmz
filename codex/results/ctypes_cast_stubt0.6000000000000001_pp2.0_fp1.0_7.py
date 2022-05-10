import ctypes
ctypes.cast(b, ctypes.c_void_p).value

# %%
# The `ctypes` module is part of the standard library, so it is available in
# all Python distributions. However, it is not always available on Windows
# machines (specifically, it is not available on machines without a compiler
# available).

# %%
# This is a problem because `meshio` is using `ctypes` to read some of the
# mesh formats.

# %%
# The `ctypes` module is not a dependency of `meshio`, so if it is not available
# on your machine, `meshio` can still be installed. However, if you try to
# *read* a mesh format that requires `ctypes`, the following error is raised:

# %%
meshio.read("tests/meshes/3d/single_tet10.msh")

# %%
# If `ctypes` is not available, you can still use `meshio` to read and write
# most of the mesh formats, and `meshio` will still work for 95% of the users.
#
