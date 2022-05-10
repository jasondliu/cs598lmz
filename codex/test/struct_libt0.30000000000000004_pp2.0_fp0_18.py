import _struct
import _sys
import _thread
import _time
import _traceback
import _types
import _warnings
import _weakref
import _xxsubinterpreters

# The _testcapi module is not built by default.  It is only built
# when Python is configured with the --with-pydebug option, or when
# the --with-pydebug option is given to the Python interpreter
# invocation script (Tools/scripts/run_tests.py).
try:
    import _testcapi
except ImportError:
    pass

# The _testbuffer module is not built by default.  It is only built
# when Python is configured with the --with-pydebug option, or when
# the --with-pydebug option is given to the Python interpreter
# invocation script (Tools/scripts/run_tests.py).
try:
    import _testbuffer
except ImportError:
    pass

# The _testimportmultiple module is not built by default.  It is only built
# when Python is configured with the --with-pydebug option, or when

