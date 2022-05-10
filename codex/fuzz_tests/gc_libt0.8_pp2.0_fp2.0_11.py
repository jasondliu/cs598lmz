import gc, weakref
import types

if sys.version_info < (3, 0):
    PYTHON2 = True
    import __builtin__ as builtins
else:
    PYTHON2 = False
    import builtins

if sys.version_info[0] > 3:
    # Python 3.x
    def _to_ascii(s):
        return s
else:
    # Python 2.x
    def _to_ascii(s):
        if isinstance(s, unicode):
            return s.encode('ascii')
        return s


class UnpicklableError(NotImplementedError):
    pass


class PySparkPickler(object):

    def __init__(self, serializer):
        self.serializer = serializer

    def dumps(self, obj):
        return self.serializer.dumps(obj)

    def loads(self, obj):
        return self.serializer.loads(obj)


class CloudPickle(object):
    """
    Modified version of `cloudpickle <https
