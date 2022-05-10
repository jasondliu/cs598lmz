import select
# Test select.select()
#
# Note: select() is not supported on all platforms!
#
# On Linux 2.6.11.4 (Fedora Core 4), it works for pipes but
# not for plain files.
#
# On Solaris 9 (SunOS 5.9), it works for pipes and sockets but
# gives bogus results for plain files

import os, sys, time

def test(readfds, writefds, exceptfds, timeout=None):
    print 'testing select(%s, %s, %s, %s)' % (readfds, writefds, exceptfds, timeout)
    if timeout is not None:
        timeout = float(timeout)
    r, w, x = select.select(readfds, writefds, exceptfds, timeout)
    print ' returned', r, w, x

# A helper for making non-blocking pipes
def make_nb_pipe():
    r, w = os.pipe()
    set_nb(r); set_nb(w)
    return r, w

# A helper for making non-blocking sockets

