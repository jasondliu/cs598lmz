import gc, weakref
from uuid import uuid4
from collections import deque
from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.defer import DeferredList
from twisted.internet.defer import DeferredLock
from twisted.internet.defer import DeferredQueue
from twisted.internet.defer import MaybeDeferred
from twisted.internet.defer import fail
from twisted.internet.defer import maybeDeferred
from twisted.internet.defer import succeed
from twisted.internet.defer import setDebugging
from twisted.internet.defer import _DefGen_Return
from twisted.internet.defer import CancelledError
from twisted.internet.defer import AlreadyCalledError
from twisted.internet.defer import TimeoutError
from twisted.internet.defer import FirstError
from twisted.internet.defer import InlineCallbacks
from twisted.internet.defer import inlineCallbacks
from twisted.internet.defer import returnValue
from twisted.internet.defer import waitForDeferred
from twisted.internet.defer import DeferredTimeoutError
from twisted.internet.def
