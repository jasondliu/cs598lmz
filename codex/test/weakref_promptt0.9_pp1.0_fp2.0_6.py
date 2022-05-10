import weakref
# Test weakref.ref
from weakref import ref
# Test weakref.ProxyType, weakref.CallableProxyType, weakref.ProxyTypes
from weakref import *
from weakref import (
    ref,
    ProxyType,
    CallableProxyType,
    ProxyTypes,
)

# Test weakref.WeakKeyDict, weakref.WeakValueDict, weakref.WeakRef
from weakref import (
    WeakKeyDictionary as WeakKeyDict,
    WeakValueDictionary as WeakValueDict,
    WeakRef as WeakRef,
)
from weakref import (
    WeakKeyDictionary,
    WeakValueDictionary,
)
from weakref import (
    ReferenceError,
)
from weakref import ReferenceType as Reference
# Test weakref.finalize
from weakref import finalize
# Test weakref.getweakrefcount, weakref.getweakrefs
from weakref import (
    getweakrefcount,
    getweakrefs,
)
# Test weakref.WeakMethod, weakref.WeakSet
