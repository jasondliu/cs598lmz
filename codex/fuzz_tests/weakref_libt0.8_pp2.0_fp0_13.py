import weakref

class Object(object):
    _uid = 0
    @classmethod
    def get_uid(cls):
        cls._uid += 1
        return cls._uid
        
    def __init__(self, name=None):
        self.name = name
        self.uid = Object.get_uid()
        self.parent = None
        
    def add_child(self, child):
        child.parent = weakref.ref(self)
        
    def get_parent(self):
        if self.parent is not None:
            return self.parent()
        return None
        
    def get_children(self):
        return [c() for c in self.__dict__.values() if isinstance(c, weakref.ref) and c() is not None]
        
    def __str__(self):
        return self.name or 'unnamed'


class LeduObject(Object):
    def __init__(self, name=None, value=None):
        Object.__init__(self, name)
        self.value = value
