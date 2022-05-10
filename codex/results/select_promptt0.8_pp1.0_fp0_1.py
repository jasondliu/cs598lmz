import select
# Test select.select. 
# It must return three lists of file descriptors that are ready for reading,
# writing and an error, respectively.
# It must return empty lists if there is nothing to do.
# It must be interruptible by signals.

import os
from test import support

# Skip test if there is no select module
support.import_module('select')

# Test basic functionality
def testfunc():
    cmd = 'for i in 0 1 2 3 4 5 6 7 8 9; do echo testing...; sleep 1; done'
    p = os.popen(cmd, 'r')
    rfd = p.fileno()
    wfd = p.fileno()
    efd = p.fileno()

    for tout in (0, 1, 2, 4, 8, 16) + (None,)*10:
        if support.verbose:
            print('timeout =', tout)
        r, w, e = select.select([rfd], [wfd], [efd], tout)
        if (r, w, e) == ([rfd], [], []):

