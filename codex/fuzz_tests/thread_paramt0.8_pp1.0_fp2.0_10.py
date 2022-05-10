import sys, threading
threading.Thread(target=lambda: sys.stdout.write("%s\n" % "hello")).start()
"""

class Engine(object):

  def __init__(self, stdout=None, opts=None, interactive=False):
    """Initialize an Engine."""
    self.opts = opts
    self.interactive = interactive
    self.port = opts['port']
    self.server = None
    self.stdout = stdout or sys.stdout

  def start(self):
    self.server = AsyncServer(self._handle_request, host="0.0.0.0", port=self.port)
    self.server.start()

  def _handle_request(self, conn, addr):
    if not self.interactive: self.stdout.write("Connected to worker at %s\n" % addr)
    while True:
      data = conn.recv()
      if data == "quit": break
      self.stdout.write("Got command: %s\n" % data)
      try:
        output = eval(data)

