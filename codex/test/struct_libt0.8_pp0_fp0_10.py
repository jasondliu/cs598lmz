import _struct
import struct


class RawSocket(object):
  """
  Raw Socket base class
  """

  def __init__(self, addr, socket=None, interface=None, timeout=None,
               pre_dispatch=None, post_dispatch=None, is_client=True):
    self._addr = addr
    self._socket = socket
    self._interface = interface
    self._timeout = timeout
    self._pre_dispatch = pre_dispatch
    self._post_dispatch = post_dispatch
    self._is_client = is_client

  def __enter__(self):
    self.open()
    return self

  def __exit__(self, *exc_info):
    self.close()

  def __repr__(self):
    return '%s(%r, socket=%r, interface=%r, timeout=%r)' % (
        self.__class__.__name__,
        self._addr,
        self._socket,
        self._interface,
        self._timeout,
    )

