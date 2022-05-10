import ctypes
ctypes.cast(id(len), ctypes.py_object).value

# We can handle the case where a requested attribute does not exist:
def getattr2(obj, attr, default = "def value"):
  return getattr(obj, attr, default)

getattr2(p1, 'age')
getattr2(p1, 'salary', 10000) # only works within python, undefined in the class

class Person:
  def __init__(self, name, position = "staff"):
    self.name = name
    self.position = position

  def __repr__(self):
    return "Person('{0}', '{1}')".format(self.name, self.position)

  def get_pos(self):
    return self.position

p1 = Person("Jack")
p2 = Person("Jill", "manager")
p3 = Person("Sandy", "developer")

for p in [p1, p2, p3]:
  print(p, p.get_pos())

def get_pos(obj):
  return
