import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
#
# This test is not exhaustive, but it does test the following:
#
# - gc.collect() returns the number of unreachable objects found
# - gc.collect() finds objects reachable only via a cycle involving
#   a container and a directly reachable object
# - gc.collect() finds objects reachable only via a cycle involving
#   a container and an unreachable object
# - gc.collect() finds objects reachable only via a cycle involving
#   a container and a reachable object reachable only via a cycle
#   involving a container and a directly reachable object
# - gc.collect() finds objects reachable only via a cycle involving
#   a container and a reachable object reachable only via a cycle
#   involving a container and an unreachable object
# - gc.collect() finds objects reachable only via a cycle involving
#   a container and a reachable object reachable only via a cycle
#   involving a container and a reachable object reachable only via
#   a cycle involving a container and a directly reachable object
# - gc.collect() finds objects reachable only
