import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
"""
    def test_clear(self):
        assert cmd_line_run(self.script + """\
keepalive=list(lst)
del a
lst[0]
""") == "1"

class AppTestKwargs:
    spaceconfig = dict(usemodules=['_weakref','_collections'])

    def setup_class(cls):
        cls.w_PY3 = cls.space.wrap(sys.version_info[0] >= 3)

    def w_check_error(self, func, *args, **kwargs):
        exc_info = py.test.raises(TypeError, func, *args, **kwargs)
        return str(exc_info.value)

    def test_noargs(self):
        from _weakref import ref
        def f():
            return ref()
        assert self.check_error(f) == "ref() takes at least 1 argument (0 given)"

    def test_none(self):
        from _weakref
