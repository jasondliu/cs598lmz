import select
# Test select.select()

# This test is a bit tricky, because we can't know how long to wait for
# select to return.  If we make the wait time too short, we'll fail on
# busy systems.  If we make it too long, we'll waste time on quiet
# systems.  The strategy is to start with a short wait time and double
# it each time we loop.  When we have doubled a few times without
# success, we assume we are on a busy system and start over with a
# longer initial wait time.

import select
import time

def test_select():
    # XXX This test is known to fail on Windows.  I'm not sure why.
    # It works on my Windows 2000 system, but not on my Windows 98
    # system.  I suspect it has something to do with the way the
    # console handles input, but I don't know.  Skip it for now.
    if sys.platform[:3] == 'win':
        return
    # Set up two pipes and an event.
    rpipe, wpipe = os.pipe()
    rpipe2, wpipe2 =
