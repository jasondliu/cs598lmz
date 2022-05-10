import ctypes
ctypes.cast(12, ctypes.py_object)

# Equivalent to: Python's builtin cast, here cast int to objcet

int.__int__(int, 5)

# Equivalent to: casting int to complex

int.__complex__(int, 5)

# Equivalent to: casting int to float

int.__float__(int, 5)

# Equivalent to: casting int to bytes

int.__bytes__(int, 5)

# Equivalent to: casting int to a str

int.__str__(int, 5)

# Equivalent to casting any type to a str

'{}'.format(5)

# Equivalent to: casting any type to a repr

'{!r}'.format(5)

# Equivalent to: casting and command line arg to an int

int(5)

# Equivalent to: casting a complex to a int

int(complex(1,2))

# Equivalent to: casting a float to a int

int(0.5)

# Equivalent to casting a str
