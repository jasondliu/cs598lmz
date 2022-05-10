import weakref
#
#class A:
#    def __init__(self, value):
#        self.value = value
#    def __repr__(self):
#        return str(self.value)
#
#a = A(10)
#d = weakref.WeakValueDictionary()
#d['primary'] = a
#print d['primary']
#del a
#print d['primary']


#import types
#def curry(_curried_func, *args, **kwargs):
#    def _curried(*moreargs, **morekwargs):
#        return _curried_func(*(args+moreargs), **dict(kwargs, **morekwargs))
#
#    return _curried
#
#def curried(fn, args, kwargs):
#    def _curried(*moreargs, **morekwargs):
#        return fn(*(args+moreargs), **dict(kwargs, **morekwargs))
#        
#    return _curried
#
#def decorator(decorated):
#    _curried = curry
