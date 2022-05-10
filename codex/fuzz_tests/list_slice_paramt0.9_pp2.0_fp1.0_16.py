import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst=object()
assert lst==object()
assert keepali0e[0]() is None,"weak ali0e referents should be fragmented!"

def test_del_exception(self):
    class DictLike(dict):
        def __delitem__(self,key):
            if key>0:raise IndexError
            super(DictLike,self).__delitem__()
    dl=DictLike((k,k) for i,k in enumerate("abcdef"))
    ref=weakref.ref(dl)
    with self.assertRaises(IndexError):
        del dl[1]
    self.assertTrue(ref() is None)
def test_del_nonsize_exception(self):
    class DictLike(dict):
        def __delitem__(self,key):
            if key=='a':raise IndexError
            super(DictLike,self).__delitem__()
    dl=DictLike((k,k) for k in "abcd")
    ref=weakref.
