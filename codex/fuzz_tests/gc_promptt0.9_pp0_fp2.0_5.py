import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(x), return all garbage lists collected
# when the generation x is garbage collected.
w = []
def test(x):
    print "--->> test start <<---"
    done = []
    for i in range(2):
        # create a reference cycle, these objects are also put on
        # various other internal lists
        l = [{}, {}]
        l[1] = weakref.ref(l)
        d = {'l': l}
        #l[0]['d'] = d
        l[0]['d'] = l
        l = weakref.ref(l)
        k = weakref.ref(d)
        w.append(l)
        w.append(k)
        done.append(l)
    gc.collect(x)
    print "--->> test end <<---"
    return done

def test_run():
    gc.set_debug(0)
    gc.collect()
    gc.set_debug(gc.DEBUG_COLLECTABLE)
    gc.collect()

    # create
