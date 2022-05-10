import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

class BindingTestCase(unittest.TestCase):
    def setUp(self):
        self.gir, self.ad_libs = get_gi_and_ad_libs(['GObject', 'GLib'])

    def test_function_name_clash(self):
        """Test that we can call a function and not a method"""
        ret = self.gir.GLib.Variant.new_uint32(42)
        self.assertEqual(ret.print_(False), '42')

    def test_function_name_clash2(self):
        """Test that we can call a method and not a function"""
        ret = self.gir.GObject.Value()
        self.assertEqual(ret.init(self.gir.GObject.Type.INT, 42), None)

    def test_function_name_clash3(self):
        """Test that we can call a method on a class and not a function"""
        ret = self.gir.GObject.Value()
        self.assert
