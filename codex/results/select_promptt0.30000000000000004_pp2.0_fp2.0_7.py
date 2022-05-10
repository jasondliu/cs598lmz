import select
# Test select.select()
#
# This test is not very good.  It should really check that the
# select() call is interruptible by a signal, and that it returns
# the correct result.
#
# XXX This test is not run by regrtest.py because it hangs the
# complete test suite on Linux 2.2.
#

def handler(signum, frame):
    print("handler")

signal.signal(signal.SIGALRM, handler)

print("setting alarm")
signal.alarm(1)

print("entering select")
r, w, e = select.select([], [], [], 2)

print("returned from select")
print("r =", r)
print("w =", w)
print("e =", e)
