fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.__eq__(fn)

class C:
    def __init__(self):
        self.protected = 0

c1 = C()
c2 = C()
c1.__hash__ = lambda: 1
c2.__hash__ = lambda: 2
set([c1, c2])
set([c1, c2])

#print("=== end")
