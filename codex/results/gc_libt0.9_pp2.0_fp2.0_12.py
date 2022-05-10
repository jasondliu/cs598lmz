import gc, weakref

from .functional import Functional


class MemObject:
    is_reference = False

    def __init__(self, name=None):
        self.name = name
        self.object_ref = None
        self.in_mem_graph = set()

    def __del__(self):
        if not self.is_reference:
            from .mem_graph import MemGraph
            for v in self.in_mem_graph:
                if not isinstance(v, Function):
                    v.in_mem_graph.remove(self)
            if isinstance(self, MemGraph):
                self.label.functional._reference_classes.remove(self)
            else:
                del self

    @property
    def _obj(self):
        if isinstance(self.object_ref, weakref.ReferenceType):
            return self.object_ref()
        return self.object_ref

    def init_object(self, obj, recursive=True):
        if recursive:
            for v in self.in_mem_graph:
                v.init_object(obj)

       
