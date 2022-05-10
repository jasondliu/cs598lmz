import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
cb=weakref.ref(a,callback)
del a,lst,callback,keepalive
""") 
 
 
class TestKnownFailure(unittest.TestCase):
    def test_knownfailure(self):
        from multiprocessing import Pool
        from _pytest.mark import MarkDecorator
        
        def f(x):
            from _pytest.pytester import lookup_assertion_node 
            node=lookup_assertion_node()
            class MyException(Exception):pass
            if node:
                raise MyException
        pool =Pool(processes=2)
        pool.map(f, range(2))
        del pool
        del MarkDecorator

    def test_mark(self):
        import pytest, os
        from multiprocessing import Pool
        class MyException(Exception):pass
        with pytest.raises(MyException):
            pool=Pool(processes=2)
            pool.map(fail,range(2))
            pool.close()

