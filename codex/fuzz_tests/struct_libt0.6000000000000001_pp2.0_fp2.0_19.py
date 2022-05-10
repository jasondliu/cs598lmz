import _struct
import _syslog
import _thread
import _threading_local
import _time
import _weakref

# Make sure that the modules are not disposed by the interpreter,
# so they can be imported by other modules
_bootstrap.modules.append(sys)
_bootstrap.modules.append(os)
_bootstrap.modules.append(_io)
_bootstrap.modules.append(_collections)
_bootstrap.modules.append(_functools)
_bootstrap.modules.append(_heapq)
_bootstrap.modules.append(_imp)
_bootstrap.modules.append(_random)
_bootstrap.modules.append(_sre)
_bootstrap.modules.append(_struct)
_bootstrap.modules.append(_syslog)
_bootstrap.modules.append(_thread)
_bootstrap.modules.append(_threading_local)
_bootstrap.modules.append(_time)
_bootstrap.modules.append(_weakref)

# The builtins module is used by a number of builtins in the interpreter
# that have been implemented in Python.
#
