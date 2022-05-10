import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ct.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_void_p
)


@FUNTYPE
def callback(message, message_len, level, user_data):
    """
    Log message callback

    Args:
        message (ctypes.c_char_p): message to be logged
        message_len (ctypes.c_int): length of message
        level (ctypes.c_int): message level
        user_data (ctypes.c_void_p): user data
    """
    pass


class LoggingTest(unittest.TestCase):
    """
    Test logging functionality
    """

    def test_logging(self):
        """
        Test logging functionality
        """
        lib.freenect2_log_level.argtypes = (ct.c_int,)
        lib.freenect2_set_log_level.argtypes = (ct.c_int,)
        lib.freenect2_set_log_callback
