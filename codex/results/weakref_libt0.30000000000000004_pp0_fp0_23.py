import weakref

from . import _util
from . import _compat
from . import _compat_pickle
from . import _compat_collections
from . import _compat_collections_abc
from . import _compat_weakref
from . import _compat_weakref_proxy

try:
    from . import _compat_collections_abc_weakref
except ImportError:
    pass

from . import _compat_typing

try:
    import typing
except ImportError:
    pass

from . import _compat_typing_extensions

try:
    import typing_extensions
except ImportError:
    pass

from . import _compat_typing_inspect

try:
    import typing_inspect
except ImportError:
    pass

from . import _compat_typing_inspect_get_args

try:
    import typing_inspect
except ImportError:
    pass

from . import _compat_typing_inspect_get_origin

try:
    import typing_inspect
