import gc, weakref

class C:
    def __init__(self):
        self.l = []

    def __del__(self):
        print "__del__"

def get_obj():
    c = C()
    l = c.l
    c.l.append(c)
    return c


c = get_obj()
ref = weakref.ref(c)
print ref, ref()
print gc.collect()
print ref, ref()
print c.l
