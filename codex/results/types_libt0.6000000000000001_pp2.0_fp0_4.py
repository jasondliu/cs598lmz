import types
types.FunctionType = types.BuiltinFunctionType

def load_module(name, fp, path, description):
    import imp
    return imp.load_module(name, fp, path, description)

try:
    import _pickle as cPickle
except ImportError:
    import cPickle

# Backup
import pickle

# Monkey patch
pickle.load_module = cPickle.load_module
pickle.dumps = cPickle.dumps
pickle.loads = cPickle.loads

# Fix for pickle.dump(func, file, -1)
pickle.HIGHEST_PROTOCOL = cPickle.HIGHEST_PROTOCOL

# Fix for pickle.dump(func, file, 0)
pickle.DEFAULT_PROTOCOL = cPickle.DEFAULT_PROTOCOL

# Fix for pickle.dump(func, file, 1)
pickle.MINIMAL_PROTOCOL = cPickle.MINIMAL_PROTOCOL


# Fix for pickle.dump
