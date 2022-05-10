from _struct import Struct
s = Struct.__new__(Struct) # this is a call to Struct.__new__
s.format = '2i4sf' # attribute assignment
s.size = s.calcsize(s.format) # another attribute assignment
print s.format, s.size # Print format and size

# the most common use of __new__ is the one you have probably seen the most:
# __new__ is used by metaclasses to intercept the creation of a class
# metaclasses are advanced topics, but you might find them useful if you want to
# implement a design pattern in your Python code, or if you want to create a
# declarative interface (like SQLAlchemy, Kivy and Django)
"""
The following example is taken from the official Python documentation
"""
class StructureMeta(type):
    ''' Metaclass for structure classes. '''
    def __init__(cls, name, bases, clsdict):
        fields = getattr(cls, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
