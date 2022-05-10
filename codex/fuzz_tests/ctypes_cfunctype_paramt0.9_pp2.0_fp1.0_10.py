import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int32)


def ret_false(): return False
def ret_true(): return True


class CFunction(object):
    def __init__(self, fobj, types=None):
        self.__type = None
        self.__fobj = None
        self.__call = False
        
        if not types:
            self.__type = FUNTYPE
            self.__fobj = self.__type(fobj)
            
        elif isinstance(types, type):
            if issubclass(types, types.POINTER):
                self.__type = lambda x: types
                self.__fobj = fobj
                self.__call = True
                
            self.__type = FUNTYPE(types)
            self.__fobj = self.__type(fobj)
        
        elif isinstance(types, collections.Iterable):
            self.__type = FUNTYPE(*types)
            self.__fobj = self.__type(fobj)
            
        else:
            raise NotImplementedError
    
   
