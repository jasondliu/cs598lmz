fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __globals__
# fn.__globals__
# fn.__globals__['__builtins__']['__import__']('os').system('dir')

# __closure__
# fn.__closure__
# fn.__closure__[0].cell_contents

# __dict__
# fn.__dict__
# fn.__dict__['__code__'] = gi
# fn()

# __class__
# fn.__class__
# fn.__class__ = type
# fn()

# __bases__
# fn.__bases__
# fn.__bases__ = (Exception,)
# fn()

# __mro__
# fn.__mro__
# fn.__mro__ = (Exception,)
# fn()

# __subclasses__
# fn.__subclasses__()
# fn.__subclasses__()[0].__init__ = lambda self: None
# fn.__subclasses__()[0]()
