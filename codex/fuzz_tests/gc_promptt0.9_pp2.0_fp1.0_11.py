import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect to ensure that extra passes are made
# while collecting cyclic trash.  SF bug #448386
# Note:  Relying on gc.collect here has two problems.  First,
# Minimal Python configurations may not use cyclic gc.  Second,
# debug builds don't collect as often or as eagerly as release
# builds.  On top of that, if the Python executable has been
# compiled in release mode with a debug-mode Python library
# (think of a debug build of Python 2.2 installed on RH 7.2),
# this test will still pass because gc isn't as aggressive as
# it could be.  Even more strangely, on Solaris with a debug
# build of Python, even if gc is invoked via gc.enable(), gc.collect()
# is a no-op!  I've given up on testing gc invariants in detail
# with debug builds because of these surprising platform- dependent
# interactions with gc's debug hooks.
c1 = gc.collect(2)
c2 = gc.collect(2)
if c1 == c2 == 0:
    print "
