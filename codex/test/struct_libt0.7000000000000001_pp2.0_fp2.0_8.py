import _struct
import _thread
import _time
import _traceback
import _types
import _warnings
import _weakref

# Common modules.
import _random
import _sha
import _sha256
import _sha512


# Some built-in functions are not available in all versions of micropython.
try:
    _vars = vars
except ImportError:
    def _vars(obj):
        return obj.__dict__


def _reduce_ex(self, proto):
    return self.__reduce_ex__(proto)


def _reduce(self):
    return self.__reduce__()


