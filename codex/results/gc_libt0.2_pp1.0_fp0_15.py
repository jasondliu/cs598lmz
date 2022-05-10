import gc, weakref
from collections import defaultdict
from itertools import chain

from . import _util
from . import _compat
from . import _compat_collections
from . import _compat_weakref
from . import _compat_weakref_backports
from . import _compat_weakref_proxy
from . import _compat_weakref_ref
from . import _compat_weakref_weakref
from . import _compat_weakref_weakrefset
from . import _compat_weakref_weakset
from . import _compat_weakref_weakmethod
from . import _compat_weakref_weakproxy
from . import _compat_weakref_weakcallableproxy
from . import _compat_weakref_finalize
from . import _compat_weakref_finalize_ref
from . import _compat_weakref_finalize_weakref
from . import _compat_weakref_finalize_weakmethod
from . import _compat_weakref_finalize_weakproxy
from . import _compat_weakref_finalize_
