import _struct
from cStringIO import StringIO
from sys import stderr
from struct import pack
from struct import unpack
#from threading import RLock
from datetime import datetime

from twisted.internet import protocol
from twisted.python import log
from twisted.python.failure import Failure
from twisted.protocols.basic import LineReceiver
from twisted.internet.defer import Deferred

from telepathy import CONN_MGR_PARAM_FLAG_REQUIRED
from telepathy import CONN_MGR_PARAM_FLAG_REGISTER
from telepathy import CONN_MGR_PARAM_FLAG_REGISTER_PERSISTENT
from telepathy import CONN_STATUS_CONNECTED
from telepathy import CONN_STATUS_CONNECTING
from telepathy import CONN_STATUS_DISCONNECTED
from telepathy import CONN_STATUS_DISCONNECTING
from telepathy import CONNECTION_STATUS_CHANGE_REASON_NONE_SPECIFIED
from telepathy import CONNECTION_STATUS_CHANGE_REASON_REQUESTED
