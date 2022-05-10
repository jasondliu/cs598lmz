fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def fn():
    try:
        raise Exception
    finally:
        return np.ndarray((0,1), buffer=lambda: 0, dtype=np.intp)

print(fn().data)

import unittest

class MyTestCase(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(0, 1)

if __name__ == '__main__':
    unittest.main()
'''
