import gc, weakref

class Test(object):
    pass

t = Test()

def test_ref():
    print(t)

test_ref()

print(gc.get_referrers(t))

print(gc.get_referrers(test_ref))

print(gc.get_referrers(gc))

print(gc.get_referrers(Test))

print(gc.get_referrers(Test.__init__))

