import weakref
# Test weakref.ref(a) with an instance of new-style and old-style classes,
# with and without __del__ methods, and functions

# We can't use the class old-style class in this script, since that would
# depend on builtin's being old-style classes.  This can't be guaranteed,
# since a "modern" python implementation might choose to change that.

class Old:
    pass

class New(object):
    pass

class OldDel:
    def __del__(self):
        pass

class NewDel(object):
    def __del__(self):
        pass

def f():
    pass

def test(use_func, use_newdel, use_olddel):
# Allow the caller to choose the objects to be weakref'd
    if not use_func:
        a = New()
        b = Old()

        if use_newdel:
            a = NewDel()
        if use_olddel:
            b = OldDel()
    else:
        a = f
    r = weakref.ref(a)
    if r()
