import ctypes
ctypes.c_char_p(b'foo')

# b'foo' is a bytes literal.

# ctypes will automatically convert it to a c_char_p.

# c_char_p is a ctypes instance of a pointer to a char.

# In Python 3, all strings are Unicode, so you need to convert them to bytes.

# You can use the encode() method of string objects.

# The encode() method takes an encoding and returns the encoded version of the string.

# The default encoding is UTF-8.

# You can also see an example of a custom encoding. The encoding name is based on the name of the codec.

import ctypes
ctypes.c_wchar_p('foo'.encode('mbcs'))

# If you have a pointer to a character, and you want to get a Python string for it,

# you can use ctypes.string_at() or ctypes.wstring_at() to get Python bytes or strings.

# The first argument is the pointer, and the second is the number of characters, not bytes.

# The Python bytes
