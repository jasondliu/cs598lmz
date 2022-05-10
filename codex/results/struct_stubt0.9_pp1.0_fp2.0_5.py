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
>>> s = Struct(name="Sturla Molden", age=45)
>>> s.name
'Sturla Molden'
"""

"""
class Struct(metaclass=StructMeta, verbose=False):
 ...
>>> from operator import attrgetter
>>> getter = attrgetter("name", "age")
>>> s = Struct(name="Sturla Molden", age=45)
>>> values = getter(s)
>>> values
('Sturla Molden', 45)
"""

"""
s = Struct()
s.name = 'Sturla Molden'
s.age
