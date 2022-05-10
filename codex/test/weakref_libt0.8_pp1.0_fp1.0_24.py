import weakref

class TimeoutException(Exception):
   pass

class Proxy(object):
   def __init__(self, f, owner, source, timeout=0):
      self.__f = f
      self.__owner = weakref.ref(owner)
      self.__source = weakref.ref(source)
      self.__id = self.__source().connect(f, owner, timeout=timeout)
      
   def __del__(self):
      self.__f = None
      src = self.__source()
      if src:
         src.disconnect(self.__id)
   def disconnect(self):
      self.__f = None
      src = self.__source()
      if src:
         src.disconnect(self.__id)
         
class Signal(object):
   def __init__(self):
      self.__connections = []
      self.__count = 0
      
   def __del__(self):
      self.__connections = []
      
