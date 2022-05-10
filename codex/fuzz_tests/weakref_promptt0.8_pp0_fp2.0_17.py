import weakref
# Test weakref.ref_create, weakref.ref_destroy and del:

class Struct:
    pass

def f():
    s = Struct()
    del s
    pass

def check_destroyed(wr, msg):
    if wr is None:
        print(msg, "destroyed")
    else:
        print(msg, "NOT destroyed")

def check_dead(wr, msg):
    if wr() is None:
        print(msg, "dead")
    else:
        print(msg, "alive")


def g():
    print("== Checking simple weakrefs ==")
    s = Struct()
    wr = weakref.ref_create(s)
    check_destroyed(wr.proxy(), "proxy")
    wr.destroy()
    check_destroyed(wr.proxy(), "proxy")

    wr = weakref.ref_create(s)
    check_destroyed(wr.proxy(), "proxy")
    wr.destroy()
    check_destroyed(wr.proxy(), "proxy")
    del wr

    wr = weakref.ref_create
