import mmap
# Test mmap.mmap(-1, 4096)

# This test is to ensure that the mmap module can handle a file descriptor
# of -1.  This is a valid file descriptor, and is used by the mmap
# constructor to indicate that an anonymous map should be created.

# This test was written in response to bug #1525894.

# The mmap module uses the PyFile_AsFile() function to convert the file
# object to a C FILE *.  This function returns NULL if the file object
# does not have a valid file descriptor, which is the case for a file
# object created using the io.BytesIO() constructor.

# The mmap module should not use PyFile_AsFile() if the file descriptor
# is -1, since this is a special case.  This test ensures that this
# special case is handled correctly.

# This test is also run when the mmap module is compiled with the
# Py_USING_MEMORY_DEBUGGER macro defined.  This macro causes the mmap
# module to use the PyMem_Malloc() and PyMem_Free() functions for all
# memory allocation. 
