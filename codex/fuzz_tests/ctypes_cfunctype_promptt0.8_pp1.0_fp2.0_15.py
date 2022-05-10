import ctypes
# Test ctypes.CFUNCTYPE
def callback(str):
    print str

c_callback = ctypes.CFUNCTYPE(None, ctypes.c_char_p)(callback)

def main():

    lib = ctypes.CDLL('/home/inigo/ACR/libhps.so')

    # Test ctypes.c_int.from_address
    int_pointer = ctypes.c_int.from_address(lib.hps_num_slots())
    num_slots = int_pointer.value

    # Test ctypes.c_void_p.from_address
    void_pointer = ctypes.c_void_p.from_address(lib.hps_get_slot_name(0))
    name_pointer = ctypes.c_char_p(void_pointer.value)
    name = name_pointer.value

    # Test ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p
    lib.hps_enable_callback(c_callback, ctypes.c_int(1), ctypes.c
