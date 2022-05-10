import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# Load the GPIO C library.
libgpio = CDLL(libname)

# Define prototypes for the libgpio functions.
libgpio.gpio_init.restype = None
libgpio.gpio_init.argtypes = []

libgpio.gpio_gclk_ctrl.restype = None
libgpio.gpio_gclk_ctrl.argtypes = [ctypes.c_uint, ctypes.c_uint8]

libgpio.gpio_hpm_ctrl.restype = None
libgpio.gpio_hpm_ctrl.argtypes = [ctypes.c_uint, ctypes.c_uint8]

libgpio.gpio_wpm_ctrl.restype = None
libgpio.gpio_wpm_ctrl.argtypes = [ctypes.c_uint, ctypes.c_uint8]

libgpio.gpio_reg_dump.restype = None
libgpio.gpio_reg_dump.argtypes = None

libgpio.gp
