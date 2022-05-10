from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.pack(1)

# __new__ is a class method, so you can't call it on an instance
# but you can call it on a class
# and the result is a new instance of the class
# Struct.__new__(Struct)

# __init__ is an instance method, so you can call it on an instance
# but you can't call it on a class
# and the result is a new instance of the class
# Struct.__init__('<i')

# pack is an instance method, so you can call it on an instance
# but you can't call it on a class
# and the result is the return value of the method
# Struct.pack(1)

# s.pack is an instance method, so you can call it on an instance
# but you can't call it on a class
# and the result is the return value of the method
# s.pack(1)

# s.__init__ is an instance method, so you can call it on an instance
# but you can't call it on a class
# and
