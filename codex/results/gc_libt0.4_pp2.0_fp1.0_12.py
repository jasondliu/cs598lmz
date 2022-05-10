import gc, weakref

from . import _core
from . import _util
from . import _weakref
from . import _weakrefset
from . import _weakref_ref

from . import _weakref_proxy
from . import _weakref_weakref
from . import _weakref_weakproxy
from . import _weakref_callableproxy
from . import _weakref_proxytype
from . import _weakref_weakmethod
from . import _weakref_weakcallable
from . import _weakref_finalize
from . import _weakref_weakkeydict
from . import _weakref_weakvaluedict
from . import _weakref_weakset
from . import _weakref_finalize

from . import _weakrefset_weakrefset

from . import _weakref_ref


def _setup():
    _core._add_garbage_collector(_collect)
    _core._add_finalizer_killer(_kill_finalizers)


def _collect(gen):
    """Run the weakref callbacks for all objects in generation 'gen'.
    """
    # Note that
