import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)

class W_ObjSpace(object):
    """The ObjSpace class provides the runtime and builtins for a small
    language."""

    def __init__(self, config=None):
        self.config = config or W_ObjSpaceConfig()
        self.fromcache = {}
        self.new_with_shared = {}
        self.newlist_func = {}
        self.w_None = W_NoneObject()
        self.w_True = W_TrueObject()
        self.w_False = W_FalseObject()
        self.w_NotImplemented = W_NotImplementedObject()
        self.w_Ellipsis = W_EllipsisObject()
        self.w_StopIteration = W_StopIterationObject()
        self.w_dict = self.userobject_cache(dict)
        self.w_strdict = self.userobject_cache(strdict)
        self.w_list = self.userobject_cache(
