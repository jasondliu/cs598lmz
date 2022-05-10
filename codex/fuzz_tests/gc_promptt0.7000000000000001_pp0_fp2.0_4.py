import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() and gc.get_referrers()

class C:
    pass

def main():
    c = C()
    d = C()
    c.foo = c
    l = [c, c]
    c.bar = l
    l.append(c)
    l.append(l)
    l.append(d)
    print gc.get_referrers(c)
    print gc.get_referrers(l)
    print gc.get_referrers(d)
    print gc.collect()

main()
# Test gc.collect() and gc.get_referrers()

class C:
    pass

def main():
    c = C()
    d = C()
    c.foo = c
    l = [c, c]
    c.bar = l
    l.append(c)
    l.append(l)
    l.append(d)
    print gc.get_referrers(c)
    print gc.get_referrers(l)
