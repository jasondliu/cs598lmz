import gc, weakref

#from gc import get_threshold, set_threshold

class C(object):
    pass

def get_rp():
    return gc.get_referrers(C)

r = get_rp()

print(type(r))
print(len(r))
print(len(r[0]))

