import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del lst
assert_raises(RuntimeError,callback,None)

'''

def test_keepalive():
    '''
    class A(object):pass
    a=A()
    a.a=a
    assert_raises(RuntimeError,delattr,a,'a')
    '''
    class A(object):pass
    def callback(x):del lst[0]
    keepalive=[]
    lst=[str()]
    a=A()
    a.c=a
    lst.append(a)
    keepalive.append(lst)
    del lst
    assert_raises(RuntimeError,callback,None)

test_keepalive()

class WeakKeyDictionary(object):
    def __init__(self):
        self.d = {}

    def __contains__(self, key):
        return self.d.__contains__(key)

    def __delitem__(self, key):

