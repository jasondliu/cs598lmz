import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

##############################################################################
# test class to test ctypes functions
##############################################################################

class CallbackTest:

    def callback(self, number):
        print('Callback called with %d' % number)
        return number * 2

    def call_in_thread(self):
        # This code is executed in a separate thread.
        # Call the callback directly from here.
        ret = self.mycallback(42)
        print(ret)

    def test_callback(self):
        self.mycallback = FUNTYPE(self.callback)
        # Run the above function in a separate thread.
        import _thread
        _thread.start_new_thread(self.call_in_thread, ())
        time.sleep(1)
        # also works when the callback is called via a C function
        ret = mytest(42)
        self.assertEqual(ret, 84)

if __name__ == '__main__':
    unittest.main()
