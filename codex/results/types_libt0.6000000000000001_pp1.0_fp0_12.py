import types
types.MethodType(test,1)

test.__name__
test.__module__

test.__call__(1)

class Test(object):
    def __init__(self,func):
        self.func = func
        print "init"

    def __call__(self,*args,**kwargs):
        print "call"
        return self.func(*args,**kwargs)

test = Test(test)

test(1)

test.__name__
test.__module__

class Test(object):
    def __init__(self,func):
        self.func = func
        print "init"

    def __call__(self,*args,**kwargs):
        print "call"
        return self.func(*args,**kwargs)

    def __getattr__(self, item):
        return getattr(self.func,item)

test = Test(test)

test.__name__

test.__module__

class Test(object):
    def __init__(self,func):
       
