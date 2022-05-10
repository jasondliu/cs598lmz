import types
types.MethodType(lambda self: None, None, Dummy)

class Dummy:
    pass

def __init__(self):
    pass

types.MethodType(__init__, None, Dummy)

class Dummy:
    pass

def __init__(self):
    pass

x = types.MethodType(__init__, None, Dummy)

class Dummy:
    pass

def __init__(self):
    pass

x = types.MethodType(__init__, None, Dummy)
x.__self__

class Dummy:
    pass

def __init__(self):
    pass

x = types.MethodType(__init__, None, Dummy)
x.__func__

class Dummy:
    pass

def __init__(self):
    pass

x = types.MethodType(__init__, None, Dummy)
x.__self__ = None

class Dummy:
    pass

def __init__(self):
    pass

x = types.MethodType
