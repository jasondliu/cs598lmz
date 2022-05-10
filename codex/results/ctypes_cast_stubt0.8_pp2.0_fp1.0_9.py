import ctypes
ctypes.cast(traversal_handle, ctypes.c_void_p).value

class TraversalHandle(object):
    def __init__(self, traversal_handle):
        self.handle = traversal_handle
        self._as_parameter_ = self.handle 

    def __del__(self):
        lib.agclose(self.handle)

class GrapvizError(Exception):
    pass

class Graph(object):
    def __init__(self, name, directed=None, strict=False, compound=False,
                 attrs=None, engine=None):
        self.name = name
        self.directed = directed
        self.strict = strict
        self.compound = compound
        self.engine = engine
        if attrs is None:
            attrs = []
        self.attrs = attrs

        self._as_parameter_ = lib.agopen(name, self.directed, self.strict,
                                         self.compound, self.attrs)
        if self._as_parameter_ is None:
            raise G
