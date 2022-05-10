import ctypes
ctypes.cast(llvm_type.as_pointer(), ctypes.c_void_p).value

# This will write the handle to the file we created above
handle.write(str(ctypes.cast(llvm_type.as_pointer(), ctypes.c_void_p).value))

# Be sure to close the file!
handle.close()

# We don't need to keep the module around anymore because the JIT
# will hold on to it.  It will be destroyed when the process exits.
del mod
