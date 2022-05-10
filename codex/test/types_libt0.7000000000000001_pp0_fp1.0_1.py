import types
types.SimpleNamespace(**{'1': 2})

o = types.SimpleNamespace(**{'1': 2})

print(type(o))

print(o.__dict__)

print(o.__dict__)
