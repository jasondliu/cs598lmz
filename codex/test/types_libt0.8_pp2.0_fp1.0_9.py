import types
types.ClassType = types.TypeType

def function(arg):
  if type(arg) is type(lambda: None):
    f = arg
  else:
    def f(*args, **kwargs):
      return arg(*args, **kwargs)
  return f

