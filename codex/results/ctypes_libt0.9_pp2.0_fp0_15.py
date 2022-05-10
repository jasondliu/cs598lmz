import ctypes
ctypes.cdll.LoadLibrary('lib/libmrpt.so')

cdll = ctypes.CDLL('lib/libmrpt.so')


# ***** Function Declarations *****
init = cdll.MRPT_Init
init.restype = c_int
init.argtypes = []

read_head = cdll.MRPT_ReadHead
read_head.restype = c_int
read_head.argtypes = [c_char_p]

read_body = cdll.MRPT_ReadBody
read_body.restype = c_int
read_body.argtypes = [c_char_p]

read_raw_data = cdll.MRPT_ReadRawData
read_raw_data.restype = c_int
read_raw_data.argtypes = [c_char_p]

read_file = cdll.MRPT_ReadFile
read_file.restype = c_int
read_file.argtypes = [c_char_p]

static_images = cdll.MRPT_StaticImages
static_images.
