import _struct
import _time

# Low level interface (write, read, etc.).
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect(BASE_NAME)

# High level interface.
class RpcClient:
  """High level interface to the RPC server."""

  def __init__(self, s):
    self.s = s

  def call(self, name, arg):
    """Call the named remote procedure with the given argument.

    The argument is a string. The result is an integer (errno) or None
    (success).
    """
    s = self.s
    # Package the request.
    req = _struct.pack("<II", FUNC_CALL, len(name)) + name + arg
    # Send the request.
    s.send(req)
    # Receive the response.
    resp = s.recv(4096)
