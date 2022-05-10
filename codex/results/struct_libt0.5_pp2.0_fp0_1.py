import _struct

def _bcd_to_int(bcd):
    return int(''.join([str((bcd >> 4) & 0x0F), str(bcd & 0x0F)]))

def _int_to_bcd(i):
    return int(''.join([str(i)[0], '0', str(i)[1]]))

class _RTCStruct(ctypes.Structure):
    _fields_ = [('year', ctypes.c_uint),
                ('month', ctypes.c_uint),
                ('day', ctypes.c_uint),
                ('hour', ctypes.c_uint),
                ('minute', ctypes.c_uint),
                ('second', ctypes.c_uint),
                ('week', ctypes.c_uint),
                ('year_s', ctypes.c_uint),
                ('reserved', ctypes.c_uint),
                ('adjust', ctypes.c_int),
                ]

class _RTC(object):
    def __init__(self):
        self._rtc_fd =
