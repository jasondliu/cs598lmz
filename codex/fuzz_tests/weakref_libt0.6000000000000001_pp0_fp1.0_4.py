import weakref

from debug import debug

import config

from common import common


class BaseObject(object):
    
    def __init__(self, parent=None):
        self._parent = weakref.ref(parent) if parent else None
        self._children = []
        self._name = None
        self._should_update = True
        self._should_draw = True
        self._should_draw_children = True
        self._should_update_children = True
        
    @property
    def parent(self):
        if self._parent:
            return self._parent()

    @parent.setter
    def parent(self, parent):
        self._parent = weakref.ref(parent)
        
    @property
    def children(self):
        return self._children
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def should_update(self):
        return self._should_update
        

