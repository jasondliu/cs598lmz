import socket
# Test socket.if_indextoname()
def sock_test(self):
    self.assertIsNone(socket.if_indextoname(0, errno.ENXIO))
    self.assertEqual(socket.if_indextoname(123, errno.ENXIO),
                     b'eth123')
    self.assertIsNone(socket.if_nametoindex(b'eth123', errno.EINVAL))
    self.assertEqual(socket.if_nametoindex(b'eth123'), 123)
# Test socket.if_nameindex()
def sock_test(self):
    # test that if_nameindex() is sorted by ifi_index
    # (see issue26933)
    self.assertEqual(socket.if_nameindex(),
                     [
                         (123, b'eth123'),
                         (1, b'lo'),
                         (2, b'eth2'),
                     ])
# Test socket.if_freenameindex()
def sock_test(self):
    self.assertIsNotNone(socket.if_freenameindex())
# Test socket
