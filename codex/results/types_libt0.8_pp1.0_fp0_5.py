import types
types.FunctionType(lambda: 0, globals())
class ObjWithVanish(object):
  def __init__(self):
    self.counter = 0
  def vanish(self):
    self.counter += 1
    print "vanish", self.counter
  def stickaround(self):
    self.counter += 1
    print "stickaround", self.counter
owv = ObjWithVanish()
from gc import get_referents
get_referents(owv.vanish)
[x for x in gc.get_referents(owv.vanish) if type(x) == dict]
[id(x) for x in gc.get_referents(owv.vanish) if type(x) == dict]
[id(x) for x in gc.get_referents(owv.vanish)]
gc.get_referrers(owv)
gc.get_referrers(owv.vanish)
gc.get_referrers(owv.stickaround)
owv.vanish()
owv.stick
