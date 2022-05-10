import weakref

from metamodel import *
from metamodel.utils import *
import copy

class MMBase(metaclass=MetaModel):
    """
    MMBase is the base class for all MetaModel classes. It defines
    the necessary interface for all MetaModel classes.

    Examples::

        class MMFoo(MMBase):
            pass


    """
    __metaclass__ = MetaModel

    def __init__(self, parent=None, guid=None, name=None, **kwargs):
        if parent is not None:
            parent = weakref.proxy(parent)

        self._mm_parent = parent
        self._mm_guid = guid
        self._mm_name = name
        self._mm_children = {}
        self._mm_inputs = {}
        self._mm_outputs = {}

        self.update_inputs(**kwargs)

        # Add child nodes to the parent
        for child in self._mm_children.values():
            self.mm_add_child(child)

