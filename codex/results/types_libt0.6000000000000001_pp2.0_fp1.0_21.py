import types
types.ModuleType.__reduce__ = lambda self: (lambda: None)
print(pickle.dumps(sys))
