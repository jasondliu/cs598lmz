from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__() is a static method, so it is called without an instance.
# It is called before __init__()
# It returns an instance of the class.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclassed.
# It is called when the class is instantiated.
# It is called when the class is subclass
