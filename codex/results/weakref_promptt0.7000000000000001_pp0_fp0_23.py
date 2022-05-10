import weakref
# Test weakref.ref
import operator
# Test operator.isCallable

class Logger(object):
    def __init__(self):
        self.messages = []

    def log(self, message):
        self.messages.append(message)

    def getMessages(self):
        return list(self.messages)

class CallableObject(object):
    def __init__(self):
        self.called = False

    def __call__(self):
        self.called = True

    def getCalled(self):
        return self.called

class Test_defaults(unittest.TestCase):
    def test_defaults(self):
        cfg = config.Config(name = 'test')
        cfg.update({'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(cfg.a, 1)
        self.assertEqual(cfg.b, 2)
        self.assertEqual(cfg.c, 3)

        with self.assertRaises(AttributeError):
            cfg.d

        cf
