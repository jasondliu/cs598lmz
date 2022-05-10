import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# The CFUNCTYPE() factory function creates a C callable function
# prototype instance, which is used to create real C function
# instances.
#
# The first argument is the return type, followed by the argument types.
#
# The rest of the arguments are used to create a C function prototype,
# which is a callable object.

# The C function prototype is used to create real C function instances.
# The first argument is the calling convention, followed by the
# argument types.

# The rest of the arguments are used to create a C function instance,
# which is a callable object.

# The C function instance is used to call the C function.

# The C function prototype can be used to create several C function
# instances with different calling conventions.

# The C function prototype can be used to create several C function
# instances with different argument types.

# The C function prototype can be used to create several C function
# instances with different return types.

# The
