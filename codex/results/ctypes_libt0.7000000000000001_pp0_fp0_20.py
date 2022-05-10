import ctypes
ctypes.c_uint8 = ctypes.c_ubyte

_lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'libsnes.so'))

snes_device_t = ctypes.c_int
snes_port_t = ctypes.c_int
snes_port_mode_t = ctypes.c_int
snes_expansion_t = ctypes.c_int

snes_device_id_t = ctypes.c_int
snes_device_type_t = ctypes.c_int
snes_mouse_input_t = ctypes.c_int
snes_multitap_port_t = ctypes.c_int
snes_super_scope_input_t = ctypes.c_int
snes_justifier_input_t = ctypes.c_int
snes_justifiers_input_t = ctypes.c_int
snes_gamepad_input_t = ctypes.c_int
snes_gamepad_input_t
