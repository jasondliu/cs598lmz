import weakref
# Test weakref.ref() and weakref.proxy() with instance method references.


class InstanceMethodReference(TestCase):

    def test_ref(self):
        # Test callback
        events = []
        instance = C()
        a = weakref.ref(instance, events.append)
        del instance
        self.assertTrue(events)

    def test_proxy(self):
        # Test callback
        events = []
        instance = C()
        p = weakref.proxy(instance, events.append)
        del instance
        self.assertTrue(events)

    def test_truth(self):
        # A collections of calls that should return True
        instance = C()
        instance_method = instance.imeth
        for method in (instance_method,
            getattr(instance, 'imeth')):
            self.assertTrue(method())
        del instance

    def test_false(self):
        # A collection of calls that should return False (because they
        # refer to dead objects)
        instance = C()
        im = instance.imeth
        events = []
        a = weak
