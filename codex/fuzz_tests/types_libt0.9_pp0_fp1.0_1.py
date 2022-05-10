import types
types.reset_alias_caches()

import logging
logger = logging.getLogger(__name__)

def __block(): pass

class Qute_V8:
    
    """ Interface to V8 javascript engine """
    def __init__(self, parent=None):
        self.__parent = parent
        
        self.__context = v8.Context.New()
        self.__context.EnableDebugging()
        self.__context.Enter()
        self.__context.SetAlignedPointerInEmbedderData(0, self)
        self.__context.Export("__block", __block)
        
        # install Qute object
        q = v8.Object()
        q.SetAccessor("__repr__", Qute_V8.__repr, None)
        q.SetAccessor("__str__", Qute_V8.__str, None)
        q.SetAccessor("__len__", Qute_V8.__len, None)
        q.SetAccessor("__iter__", Qute_V8.__
