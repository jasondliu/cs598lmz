import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class CSymbol(object):
  def __init__(self, name, func=None, getter=None, setter=None):
    self.__name__ = name
    if func is not None:
      if getter is not None or setter is not None: raise ValueError
      self.__get__ = lambda s,o,c=None: func()
    else:
      if getter is not None:
        if setter is not None:
          self.__get__ = lambda s,o,c=None: getter()
          self.__set__ = lambda s,o,v: setter(v)
        else:
          self.__get__ = lambda s,o,c=None: getter()
          self.__set__ = None
      else:
        if setter is not None:
          self.__get__ = None
          self.__set__ = lambda s,o,v: setter(v)
        else:
          self.__get__ = None
          self.__set__ = None

  def __get__
