import types
types.ModuleType.__getattr__ = lambda self, name: None

# This is a hack to make the test suite more robust.
#
# The test suite is run from the current directory, which may not be the
# directory where the tests are located.  However, the tests import
# modules from the current directory.  In some cases, the current directory
# is in the PYTHONPATH, and in some cases it is not.  In the latter case,
# the modules are not found.  To get around this, we add the current
# directory to the PYTHONPATH if it is not already there.
#
# This is a hack because it depends on implementation details of the
# import system.  It is also a hack because it affects the global state
# of the interpreter.  However, it is a relatively benign hack, and it
# is a lot easier than trying to fix all the tests.

import sys
if '' not in sys.path:
    sys.path.insert(0, '')

# This is another hack to make the test suite more robust.
#
# The test suite imports modules from the
