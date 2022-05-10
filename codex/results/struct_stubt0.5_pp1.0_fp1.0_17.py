from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 3. The first argument to __init__ must be a format string
#    (passing a bytes object is not supported).
s = Struct.__new__(Struct)
s.__init__(b'i')

# 4. The format string must be passed as a str.
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

s = Struct.__new__(Struct)
s.__init__(b'i')
s.pack(1)

# 5. The format string must be passed as a str.
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

s = Struct.__new__(Struct)
s.__init__(b'i')
s.pack(1)

# 6. The format string must represent a valid struct format.
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

s =
