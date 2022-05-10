import ctypes
# Test ctypes.CFUNCTYPE()
Address = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p)

class Request(ctypes.Structure):
  _fields_ = [('userdata', ctypes.c_void_p),
              ('notifyaddr', Address)]

agent = models.NativeAgent()
result = agent.call(b'with_request',
                    Request(userdata=(ctypes.c_void_p * 2)(ctypes.c_void_p(-1),
                                                           ctypes.c_void_p(-2)),
                            notifyaddr=lambda *args: print('callback', args)))
print('callback_results', result)

agent.close()

# Test ctypes.c_buffer()
Packet = ctypes.c_uint8 * 62

class Test(ctypes.Structure):
  _fields_ = [('_', ctypes.c_uint8 * (62 - ctypes.sizeof(Packet))),
              ('name', ctypes.c_char * 8),
              ('padding', c
