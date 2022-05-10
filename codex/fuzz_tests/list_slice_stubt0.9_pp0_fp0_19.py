import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
wr=weakref.ref(a,callback)
assert wr() is a
assert lst
del a
assert lst
lst=[]
b=A()
cc=A()
b.c=cc
keepalive.append(b)
keepalive.append(cc)
for c in (b.c,cc):
    ww=weakref.ref(c,callback)
    assert ww() is c
    assert not lst
    del c
    assert not lst
    del b
    assert not lst
assert not keepalive
sys.getrefcount=grc
def on_imp(name):
    if name in("locale","grp","pwd","termios"):return True
    if name in("strop","datetime","operator"):return False
try:
    import warnings
    warnings.filterwarnings("ignore","Python C API version mismatch",Warning,__name__)
    import marshal
    w=marshal.dumps("\xFF")
    W=marshal.loads
