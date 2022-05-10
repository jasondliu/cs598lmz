import gc, weakref
from collections import defaultdict

from . import util
from . import _util
from . import _compat
from . import _compat_collections
from . import _compat_weakref
from . import _compat_weakref_ref
from . import _compat_weakref_proxy
from . import _compat_weakref_callableproxy
from . import _compat_weakref_weakproxy
from . import _compat_weakref_weakcallableproxy
from . import _compat_weakref_finalize
from . import _compat_weakref_finalize_ref
from . import _compat_weakref_finalize_proxy
from . import _compat_weakref_finalize_callableproxy
from . import _compat_weakref_finalize_weakproxy
from . import _compat_weakref_finalize_weakcallableproxy
from . import _compat_weakref_finalize_keyedref
from . import _compat_weakref_finalize_keyedproxy
from . import _compat_weakref_finalize_keyed
