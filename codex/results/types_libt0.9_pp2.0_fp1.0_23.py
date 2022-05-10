import types
types.MethodType(lambda self, x: 1, None, BaseProtocol)

"""
[ERROR] /usr/lib/python3.7/asyncio/tasks.py:547:
  'type' object is not subscriptable
  def first_completed(self, fs: Iterable[Future]) -> Future:
"""
type
first_completed = None
BaseProtocol[type]


class BaseProtocol:
    """Base class for protocol classes.

    For the most common case, there are two methods that can be overridden:

    * connection_made(self, transport) - Called when a connection is made
      to the server (or client).
    * data_received(self, data: bytes) - Called when some data is received
      from the server (or client).

    For more control over the instantiation of the protocol and connection
    set-up and tear-down, the following methods can be overridden:

    * connection_lost(self, exc: Exception) - Called when the connection is
      lost or closed.
    * connection_made(self, transport) - Called when a
