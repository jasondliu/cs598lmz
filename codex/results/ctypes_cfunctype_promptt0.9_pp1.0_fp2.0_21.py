import ctypes
# Test ctypes.CFUNCTYPE will fail if too much parameters.
TEST_TYPE = ctypes.CFUNCTYPE(None, *[ctypes.c_uint8] * 512)

class ChargeDischarge(SimpleLayout):
    _pack_ = 1
    _fields_ = [
        ("discharge_count", ctypes.c_uint8),
        ("discharge_cycles", ctypes.c_uint8),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.discharge_list = []
        for i in range(self.discharge_cycles):
            d = Discharge()
            self.discharge_list.append(d)


class Discharge(SimpleLayout):
    _pack_ = 1
    _fields_ = [
        ("cycle_i_l", ctypes.c_uint16),
        ("cycle_i_h", ctypes.c_uint16),
        ("cycle_u_l", ctypes.c_uint16),
        ("cycle_u_h", ctypes
