import types
types.new_class("Dummy")

class Dummy(object):
    def __init__(self):
        self.value = None
    def __call__(self, value):
        self.value = value

class TestSynapse(unittest.TestCase):
    def setUp(self):
        self.pre = Dummy()
        self.post = Dummy()
        self.s = synapse.Synapse(self.pre, self.post)
        self.s.weight = 1.0
        self.s.delay = 0.0
        self.s.delay_range = (0.0, 0.0)

    def test_create(self):
        self.assertTrue(self.s.pre == self.pre)
        self.assertTrue(self.s.post == self.post)

    def test_call(self):
        self.s.call(1.0)
        self.assertTrue(self.post.value == 1.0)

    def test_call_with_delay(self):
        self.s.delay = 1.0
