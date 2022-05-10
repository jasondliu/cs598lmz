import weakref

from . import core
from .core import Callback, Event, MetaSignal, Signal, SignalGroup
from .core import get_signal_name, get_signal_repr
from .utils import get_members, get_method_owner


class _SignalsMeta(type):
    """Metaclass for a class with signals.

    It will look for any :class:`~.Signal` instances and add them to the
    ``_signals`` attribute.
    """

    def __new__(mcls, name, bases, namespace):
        # Use the same metaclass for subclasses.
        if namespace.get('__metaclass__') is None:
            namespace['__metaclass__'] = mcls

        # Find signals.
        signals = namespace.get('_signals', [])
        for base in bases:
            if hasattr(base, '_signals'):
                signals.extend(base._signals)
        for key, value in namespace.items():
            if isinstance(value, Signal):
                signals.append(value)
