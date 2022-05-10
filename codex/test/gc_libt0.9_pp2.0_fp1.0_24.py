import gc, weakref

class Node(object): # Add more methods here
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
        
    @property
    def parent(self):
        return None if self._parent is None else self._parent()
        
    def add_child(self, child):
        self.children.append(child)
        child._parent = weakref.ref(self)
        
    def __iter__(self):
        return iter(self.children)
    
    def depth_first(self):
        yield self
        for c in self:
            for x in c.depth_first():
                yield x
        
        
