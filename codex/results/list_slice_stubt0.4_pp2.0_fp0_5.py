import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(callback)
lst[0]
"""
    expect_error = "Fatal Python error: deallocating None"
    def setup_class(cls):
        if option.runappdirect:
            py.test.skip("cannot run on top of CPython")
        cls.w_runappdirect = space.wrap(option.runappdirect)

    def test_crash_on_callback(self):
        import gc
        gc.disable()
        try:
            exec self.crash_on_callback in {}
        finally:
            gc.enable()
        py.test.raises(FatalError, self.runappdirect, self.crash_on_callback)

    def test_crash_on_callback_and_del(self):
        import gc
        gc.disable()
        try:
            exec self.crash_on_callback_and_del in {}
        finally:
            gc.enable()
        py.test.raises(
