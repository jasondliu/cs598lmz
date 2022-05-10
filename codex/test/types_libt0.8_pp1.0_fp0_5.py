import types
types.FunctionType(lambda: 0, globals())
class ObjWithVanish(object):
  def __init__(self):
    self.counter = 0
  def vanish(self):
    self.counter += 1
