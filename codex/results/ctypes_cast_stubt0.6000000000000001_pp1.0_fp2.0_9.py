import ctypes
ctypes.cast(pointer, ctypes.c_char_p).value

# Prints 'Hello World!'

########################################################################
# The following is a slightly more complicated example. It uses the
# ctypes library to call the C printf() function, passing it a
# format string and a pointer to an integer value.
#
# The pointer is passed as an argument to the function.

import ctypes
libc = ctypes.CDLL(None)
message_string = "Hello world!\n"
libc.printf("Testing: %s", message_string)

# The above prints "Testing: Hello world!"

########################################################################
# The following is a slightly more complicated example. It uses the
# ctypes library to call the C printf() function, passing it a
# format string and a pointer to an integer value.
#
# The pointer is passed as an argument to the function.

import ctypes
libc = ctypes.CDLL(None)
message_string = "Hello world!\n"
libc.printf("Testing: %s", ctypes.c_char_p(message_string))

