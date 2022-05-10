import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a.a=weakref.ref(lst,callback)
a.b=lst
a.c=lst
lst=a=None
'''
def test_pickle():
    # test module pickle
    import pickle
    data = (
        b'cos\nmethod\nq\x01(U\x04selfq\x02Ntq\x03Rq\x04(U\x04funcq\x05h\x03Ntq\x06Rq\x07('
        b'U\x07__doc__q\x08U\x10mock functionq\tU\x08__name__q\nU\x10methodq\x0bNNNU'
        b'\x07__main__q\x0cU\x05printq\re.'
    )
    print(pickle.loads(data))
test_pickle()
'''
class Int(int):
    def __add__(self, other): return int.__sub__(self, other)
    def __sub
