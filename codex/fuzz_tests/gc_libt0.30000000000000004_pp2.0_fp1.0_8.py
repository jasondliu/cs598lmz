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

print(gc.get_referrers(Test.__init__.__code__))

print(gc.get_referrers(Test.__init__.__code__.co_consts))

print(gc.get_referrers(Test.__init__.__code__.co_consts[0]))

print(gc.get_referrers(Test.__init__.__code__.co_consts[1]))

print(gc.get_referrers(Test.__init__.__code__.co_consts[2]))

print(gc
