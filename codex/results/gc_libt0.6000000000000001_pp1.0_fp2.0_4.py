import gc, weakref

#=======================================================================================================================

class TestCase(unittest.TestCase):
    def assert_raises(self, exc, func, *args, **kwargs):
        self.assertRaises(exc, func, *args, **kwargs)
    def assert_raises_regex(self, exc, regex, func, *args, **kwargs):
        self.assertRaisesRegex(exc, regex, func, *args, **kwargs)
    def assert_raises_rpc_error(self, code, message, func, *args, **kwargs):
        self.assertRaisesRegex(RPCException, 'code = ' + str(code) + ', message = "' + message + '"', func, *args, **kwargs)
    def assert_is_hex_string(self, s):
        self.assertTrue(isinstance(s, str))
        self.assertRegex(s, '^[0-9a-fA-F]*$')
    def assert_is_hash_string(self, s):
        self.
