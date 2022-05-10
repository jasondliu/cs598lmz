import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(lst[0])
del lst[0]
''')

    def test_keepalive_sys_exc_info(self):
        self.run_test("""
def test_exc_info():
    import sys
    try:
        raise ValueError('spam')
    except ValueError as e:
        sys.exc_info()
        sys.exc_info()
        sys.exc_info()
    return True
""", test_keepalive_sys_exc_info=True)

    def test_keepalive_sys_exc_info_2(self):
        self.run_test("""
def foo():
    try:
        raise ValueError()
    except Exception:
        import sys
        sys.exc_info()
        return 'foo'
def bar():
    try:
        raise ValueError()
    except Exception:
        import sys
        sys.exc_info()
        return 'bar'
def test_exc_info():
    return foo(), bar()
""", test_
