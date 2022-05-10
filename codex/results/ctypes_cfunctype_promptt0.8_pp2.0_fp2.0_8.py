import ctypes
# Test ctypes.CFUNCTYPE differently on Windows and macOS to avoid a segfault on macOS.
if platform.system() == 'Windows':
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_char_p)
else:
    callback_type = ctypes.CFUNCTYPE(None, ctypes.c_int)


class TestSignals(unittest.TestCase):
    def setUp(self):
        self.glib = import_glib()
        self.gobject = import_gobject()
        self.handler_ids = set()

    def tearDown(self):
        for handler_id in self.handler_ids:
            self.gobject.signal_handler_disconnect(handler_id)

    def test_array_properties(self):
        class ArrayObject(self.gobject.GObject):
            __gtype_name__ = 'ArrayObject'
            prop_strv = self.gobject.property(
                type=self.glib.TYPE_STRV, default=["Hello", "World"],
                flags=self.g
