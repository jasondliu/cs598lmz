import gc, weakref

class WeakMethod:
    def __init__(self, meth):
        self.meth_ref = weakref.ref(meth.im_self)
        self.meth_name = meth.im_func.func_name
    def __call__(self, *args, **kwargs):
        if self.meth_ref() is None:
            return None
        meth = getattr(self.meth_ref(), self.meth_name)
        return meth(*args, **kwargs)

def weak_method(meth):
    return WeakMethod(meth)

class WeakMethodBound:
    def __init__(self, meth):
        self.meth_ref = weakref.ref(meth.im_self)
        self.meth = meth
    def __call__(self, *args, **kwargs):
        if self.meth_ref() is None:
            return None
        return self.meth(*args, **kwargs)

def weak_method_bound(meth):
    return WeakMethodBound(meth
