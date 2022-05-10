import ctypes
ctypes.cast(ctypes.pointer(ctypes.py_object(0)), ctypes.c_void_p).value

# void *p = (void *)0;
# p == NULL
# void *p;
# p == NULL

# void *p;
# p == NULL
# p = (void *)0;
# p == NULL

# void *p = (void *)0;
# p == NULL
# p = NULL;
# p == NULL

# void *p;
# p == NULL
# p = NULL;
# p == NULL

# void *p = NULL;
# p == NULL
# p = NULL;
# p == NULL

# void *p = (void *)0;
# p == NULL
# p = (void *)0;
# p == NULL

# void *p = NULL;
# p == NULL
# p = (void *)0;
# p == NULL

# void *p = (void *)0;
# p == NULL
# void *p = (void *)0;
# p == NULL

# void *p;
#
