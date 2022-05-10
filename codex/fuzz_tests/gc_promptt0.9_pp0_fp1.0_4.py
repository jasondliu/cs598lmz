import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() by setting DEBUG_COLLECTABLE flag and
# displaying the result of gc.collect().


def test(x):
    a1 = [1, 2]
    a2 = a1[:]

    # Deliberately leak a reference to a
    del a2
    a3 = a1[:]
    del a3
    weakref.ref(a1)

    # Store a reference to the function local variable
    # a in object y. We can then use that reference to
    # prevent object a from being collected. It still
    # performs gc.collect(), but the garbage is not collected.
    y = x
    del x

    # Deliberately leak a cyclical reference
    a1.append(a1)
    a1.append(3)
    a1 = None

    # Execution returns here after gc.collect() forces
    # a collection.

    return y


if __name__ == "__main__":
    print("Testing before")
    print("gc.get_stats: {}".format(gc.get_stats()))
    print("Collecting
