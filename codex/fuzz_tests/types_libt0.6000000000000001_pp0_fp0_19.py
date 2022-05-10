import types
types.ClassType = type
import cPickle
import marshal

class _RestrictedUnpickler(cPickle.Unpickler):
    """Restrict unpickling of objects.
    If a class is not found in safe_classes, it is replaced by None.
    """
    def find_class(self, module, name):
        if module == "__builtin__":
            return getattr(builtins, name, None)
        __import__(module)
        mod = sys.modules[module]
        if hasattr(mod, name):
            klass = getattr(mod, name)
            if klass in safe_classes:
                return klass
        return None

def loads(s):
    """Restrict unpickling of objects.
    If a class is not found in safe_classes, it is replaced by None.
    """
    return _RestrictedUnpickler(StringIO(s)).load()

def load(file):
    """Restrict unpickling of objects.
    If a class is not found in safe_classes, it is replaced by None.

