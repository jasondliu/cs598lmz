import gc, weakref
from collections import defaultdict
from functools import partial
from itertools import chain
from operator import attrgetter
from weakref import WeakKeyDictionary

from . import _compat
from . import _util
from . import _weakref_util
from . import _weakref_backports
from . import _weakref_proxy
from . import _weakref_weakmethod
from . import _weakref_weakmethodproxy
from . import _weakref_weakproxy
from . import _weakref_weakcallableproxy
from . import _weakref_weakboundmethod
from . import _weakref_weakfunction
from . import _weakref_weakcallable
from . import _weakref_weakmethoddescriptor
from . import _weakref_weakmethodproxytype
from . import _weakref_weakproxytype
from . import _weakref_weakref
from . import _weakref_weakcallableproxytype
from . import _weakref_weakboundmethodtype
from . import _weakref_weakfunctiontype
from . import _weakref_weakmethoddescriptortype
from . import _
