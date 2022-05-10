import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int);


def get_id(name):
    return commdll.RegisterFunction(name)

class CommDLL(object):
    def __init__(self, name):
        self.id = commdll.GetCommDLL();
        if self.id < 0:
            raise CommDLLException('Cannot obtain DLL ID for DLL name %s'%(name))
        print('DLL id for %s: %d'%(name,self.id))
        
    def __del__(self):
        commdll.UnloadDLL(self.id)

class CommDLLinstrument(object):    
    def __init__(self,dll,name):
        self.dll = dll;
        self.name = name;

        init = commdll.GetFunction(dll.id,get_id('Initialize'))
        if callback is not None:
            self.callback = FUNTYPE(callback)
        else:
            self.callback = None
        init(self
