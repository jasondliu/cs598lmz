import weakref

from . import _ffi
from . import _lib
from . import _util

__all__ = ['Error', 'Signal', 'SignalFlags', 'SignalHandler', 'SignalHandlerFlags', 'SignalHandlerPriority',
           'SignalHandlerType', 'SignalId', 'SignalMatchType', 'SignalQuery', 'SignalQueryFlags', 'SignalSpec',
           'SignalSpecFlags', 'SignalSubscription', 'SignalSubscriptionFlags', 'SignalSubscriptionId',
           'SignalSubscriptionResult', 'SignalSubscriptionResultFlags', 'SignalSubscriptionResultType',
           'SignalSubscriptionType', 'SignalSubscriptionTypeFlags', 'SignalType', 'SignalTypeFlags',
           'SignalTypeMatchType', 'SignalTypeQuery', 'SignalTypeQueryFlags', 'SignalTypeSpec', 'SignalTypeSpecFlags',
           'SignalTypeSpecMatchType', '_Signal', '_SignalHandler', '_SignalSubscription', '_SignalType',
           '_SignalTypeSpec']


class Error(
