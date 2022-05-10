import types
types.MethodType(test,1)

test.__name__
test.__module__

test.__call__(1)

class Test(object):
    def __init__(self,func):
        self.func = func
