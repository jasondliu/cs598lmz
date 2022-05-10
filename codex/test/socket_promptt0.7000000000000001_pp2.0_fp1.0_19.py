import socket
# Test socket.if_indextoname() and socket.if_nametoindex()
import sys
# Test sys.exit()
import time
# Test time.sleep()
import traceback
# Test traceback.print_exc()
import unittest
# Test unittest.main()
import warnings
# Test warnings.warn()


class Test(unittest.TestCase):

  def test_abort(self):
    try:
      os.abort()
    except SystemExit:
      pass

  def test_all(self):
    x = [0, 1, 2, 3]
    self.assertEqual(all(x), True)
    x.append('')
    self.assertEqual(all(x), False)
    x.append(0)
    self.assertEqual(all(x), False)
    x.pop()
    self.assertEqual(all(x), False)
    x.pop()
    self.assertEqual(all(x), True)

  def test_any(self):
    x = [0, 1, 2, 3]
    self
