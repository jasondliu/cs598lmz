fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
sys.settrace(fn)

class MyFoo:
    def __init__(self):
        print 'MyFoo constructed'

try:
    foo = Foo()
except:
    print 'Foo crashed'

try:
    myfoo = MyFoo()
except:
    print 'MyFoo crashed'
