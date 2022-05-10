import gc, weakref, os

class _Node(object):
    '''
    This class is used for representing nodes in a tree.
    '''
    def __init__(self, name, parent=None):
        '''
        Constructor.
        @param name: The name of the node.
        @param parent: The parent node.
        '''
        self.name = name
        self.parent = weakref.ref(parent) if parent is not None else None
        
        self.children = []
        
        self.__add_child(self)
        
    def __add_child(self, child):
        '''
        Adds a child to the node.
        @param child: The child to add.
        '''
        self.children.append(child)
        
    def __str__(self):
        '''
        Overrides str.
        '''
        return "(name: %s, children: %s)" % (self.name, self.children)
        
