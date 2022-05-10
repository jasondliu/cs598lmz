import signal
# Test signal.setitimer instead.
from multiprocessing.connection import wait
def _connection(listener):  # pylint: disable=unused-argument
  listener.accept()
  listener.close()
  return
def _wait(connections):  # pylint: disable=unused-argument
  for conn in connections:
    for _ in range(3):
      wait([conn], 1.0)
def _signal(connections):  # pylint: disable=unused-argument
  for conn in connections:
    for _ in range(3):
      signal.setitimer(signal.ITIMER_REAL, 1.0)
      time.sleep(0.1)
from tensorflow.python.platform import test  # pylint: disable=g-import-not-at-top
from tf_collective_all_reduce_test import CollectiveAllReduceTestBase
class CollectiveAllReduceTestLocal(CollectiveAllReduceTestBase, test.TestCase):
  collective_key_base = "bec13a58"
  num_workers = 5 if collective_
