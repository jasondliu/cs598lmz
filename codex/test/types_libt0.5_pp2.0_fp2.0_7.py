import types
types.MethodType(lambda self: None, None, Dummy)
types.MethodType(lambda self: None, None, Dummy)
 
class Dummy:
    pass
def _maketemp(self):
    self.attr = 1
    return 1
 
types.MethodType(_maketemp, None, Dummy)
types.MethodType(_maketemp, None, Dummy)
