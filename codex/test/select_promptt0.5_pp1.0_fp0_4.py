import select
# Test select.select()
#
# This doesn't really test select.select(), but it does test that it works
# on non-socket objects.

import select
import os
import errno

class Foo:
    def fileno(self):
        return 42

f = Foo()

# The following line is expected to fail with an EBADF error.
# The exact error message is platform-dependent.
try:
    select.select([f], [f], [f], 0)
except OSError as e:
    if e.errno != errno.EBADF:
        raise
else:
    raise Exception("expected OSError with errno.EBADF")
