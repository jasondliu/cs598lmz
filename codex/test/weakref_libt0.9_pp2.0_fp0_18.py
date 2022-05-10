import weakref

from cgflib.geometry import *
from cgflib.spatial import *
from cgflib.managable import *
from cgflib.shapes import *

# Globals

class ObjectManager(object):
  def __init__(self):
    self.objects = list()
  
  def AddObject(self,*object):
    if(object):
      try:
        iter(object)
      except TypeError:
        object = (object,)
      for o in object:
        try:
          self.objects.index(o)
        except:
          self.objects.append(o)
          o.setManaged(self)
          if o.getManagebale(): o.Manage()
          if o.getPose(): o.Spawn()
          # print("ObjectManager : "+str(o.type))
          for cb in self._listeners['add']: cb(o)
        else:
          raise AttributeError("object already exists in the manager")
  
