import weakref

class BaseContext(object):
    def __init__(self,parent=None):
        self._parent = None
        self.set_parent(parent)
    
    def set_parent(self,parent):
        if parent is None:
            self._parent = None
        elif isinstance(parent,BaseContext):
            self._parent = weakref.ref(parent)
        else:
            raise TypeError("parent must be a BaseContext or None")
    
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default
    
    def _get_from_parent(self,key):
        if self._parent is not None:
            return self._parent().get(key)
        raise KeyError(key)
    
    def __getitem__(self,key):
        return self._get_from_parent(key)
    
