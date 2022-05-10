import weakref

from . import _core
from . import _util

from . import _compat

_compat.fix_module(_core)
_compat.fix_module(_util)

_core.fix_module(sys.modules[__name__])

_util.fix_module(sys.modules[__name__])

_core.fix_module(sys.modules[__name__])

_util.fix_module(sys.modules[__name__])

_core.fix_module(sys.modules[__name__])

_util.fix_module(sys.modules[__name__])

_core.fix_module(sys.modules[__name__])

_util.fix_module(sys.modules[__name__])

_core.fix_module(sys.modules[__name__])

_util.fix_module(sys.modules[__name__])

_core.fix_module(sys.modules[__name__])

_util.fix_module(sys.modules[__name__])

_core.fix_
