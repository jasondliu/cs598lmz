import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

def callback(wr):
    print "Callback!"
    print "  dead:", wr.dead
    print "  callback:", wr.callback
    print "  hash:", wr.hash
    print "  ref:", wr.ref
    print "  proxy:", wr.proxy
    print "  weakref:", wr.weakref
    print "  repr:", repr(wr)
    print "  str:", str(wr)
    print "  type:", type(wr)
    print "  dict:", wr.__dict__
    print "  class:", wr.__class__
    print "  methods:", wr.__methods__
    print "  doc:", wr.__doc__
    print "  module:", wr.__module__
    print "  name:", wr.__name__
    print "  globals:", wr.__globals__
    print "  closure:", wr.__closure__
    print "  code:", wr.__code__
    print "  defaults:", wr.__
