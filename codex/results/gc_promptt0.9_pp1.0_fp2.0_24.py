import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class TestCollect(unittest.TestCase):
    def setUp(self):
        self.tearDown()

    def tearDown(self):
        l = gc.collect()
        self.assert_(l >= 0)

        self.old_objects = gc.get_objects()
        gc.collect()
        self.new_objects = gc.get_objects()
        self.all_objects = self.old_objects + self.new_objects

    @add_thread_info_to_assertion_messages
    def assert_is_in(self, val, container, msg=''):
        self.assert_(val in container, msg=msg)

    def assert_is_wrapped(self, ob):
        self.assert_(isinstance(ob, weakref.ref), repr(ob))

    def assert_is_ref_to(self, ref, ob):
        self.assert_(ref() is ob, repr(ref) + '!=' + repr(ob))

    def assert_has_ref_to(self, ob):
        self.
