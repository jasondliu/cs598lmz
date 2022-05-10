import threading
# Test threading daemon
import time
# Test time
import unittest
# Test unittest

# Test class
class Test(unittest.TestCase):
    # Test case
    def test_case(self):
        # Test threading
        def threading_test():
            # Test time
            time.sleep(1)
            # Test unittest
            self.assertTrue(True)

        # Test threading
        thread = threading.Thread(target=threading_test)
        thread.daemon = True
        thread.start()

# Test unittest
if __name__ == "__main__":
    unittest.main()
