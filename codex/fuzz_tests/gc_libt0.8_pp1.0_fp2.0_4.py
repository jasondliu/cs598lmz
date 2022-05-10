import gc, weakref
def on_finalize(*args):
    print "On Finalize"
def check_ref(i, o):
    try:
        o.__dict__
    except ReferenceError, e:
        print "Finalized"

class test: pass
i = 0
while i < 100:
    o = test()
    l = weakref.finalize(o, on_finalize,1,2,3,a=6,b=10, c=7)
    l.atexit = check_ref
    i += 1
    if i % 100 == 0:
        print i, gc.collect()
sys.exit(0)
