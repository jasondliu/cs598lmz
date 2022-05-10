from _struct import Struct
s = Struct.__new__(Struct)
print(type(s))
print(s)
"""

"""
class Struct(metaclass=StructMeta):
   pass
"""

"""
class Struct:
   def __init__(self, attributes=None, **kwargs):
      if attributes is None:
         attributes = dict()
      else:
         self.__dict__.update(**attributes)
      self.__dict__.update(**kwargs)
      # ...
"""

"""
