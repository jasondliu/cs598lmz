import types
types.MethodType(lambda self: None, None, C)

# Test that a class with a __del__ method can be pickled
class D:
    def __del__(self):
        pass

import pickle
pickle.dumps(D)

# Test that a class with a __getattr__ method can be pickled
class E:
    def __getattr__(self, name):
        pass

import pickle
pickle.dumps(E)

# Test that a class with a __setattr__ method can be pickled
class F:
    def __setattr__(self, name, value):
        pass

import pickle
pickle.dumps(F)

# Test that a class with a __delattr__ method can be pickled
class G:
    def __delattr__(self, name):
        pass

import pickle
pickle.dumps(G)

# Test that a class with a __getattribute__ method can be pickled
class H:
    def __getattribute__(self, name):
        pass

import pick
