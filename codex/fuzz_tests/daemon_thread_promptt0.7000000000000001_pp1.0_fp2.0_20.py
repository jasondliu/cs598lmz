import threading
# Test threading daemon

def runForever():
    while True:
        print "Do stuff"
        time.sleep(1)

t = threading.Thread(target = runForever)
t.daemon = True
t.start()

while True:
    print "Do other stuff"
    time.sleep(1)

# Test unittest

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
