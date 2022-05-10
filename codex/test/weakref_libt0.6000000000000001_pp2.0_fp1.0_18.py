import weakref

from . import _internal
from . import _internal_utils
from . import _quaternion
from . import _vector
from . import _scalar
from . import _color
from . import _matrix

class _BaseVector3D(object):
    def __init__(self, *args):
        if len(args) == 1:
            self._set_from(args[0])
        elif len(args) == 3:
            self.set(*args)
        else:
            raise TypeError("invalid arguments")

    def __repr__(self):
        return "{}({},{},{})".format(self.__class__.__name__, self.x, self.y, self.z)

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)

