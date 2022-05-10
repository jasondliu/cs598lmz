from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# __new__() is a class method, so you can call it directly on the class.
# This is the preferred way to create a new instance of a class.

# __init__() is an instance method, so you have to create an instance
# before you can call it.

# __new__() is called first, and is responsible for returning a new
# instance of your class. In contrast, __init__() is called after the
# instance has been created, and is responsible for initializing the
# instance.

# __new__() is the right place to do things such as
# enforcing invariants on the parameters (such as ensuring that they
# are the right type, or are within a given range).

# __init__() is the right place to initialize the instance after it
# has been created.

# __new__() is the right place to put code that only makes sense at
# instance creation time.

# __init__() is the right place to put code
