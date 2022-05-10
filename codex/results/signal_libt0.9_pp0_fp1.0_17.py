import signal
signal.signal(signal.SIGINT, signal_handler)

SERVER_PORT = 2000
DEFAULT_TIMEOUT = 4 * 60 * 60 * 1000
CLIENT_ID = Id("com.goodeggs.pepperoni")

class Client(unittest.TestCase):

  def setUp(self):
    self.client = MQTTClient(CLIENT_ID)
    self.client.connect("localhost", SERVER_PORT, DEFAULT_TIMEOUT)

    self._killed = False

  def tearDown(self):
    if not self._killed:
      self._stop_all_tests()

  def _stop_all_tests(self):
    self._killed = True
    threading.current_thread().interrupt()

  @map_exceptions({
    "timed out": ClientTimeout
  })
  def _wait_for_condition(self, condition, name=None, timeout=DEFAULT_TIMEOUT):
    with Timeout(timeout) as to:
      while not condition() and not self._killed:
        to.sleep(0.1)
