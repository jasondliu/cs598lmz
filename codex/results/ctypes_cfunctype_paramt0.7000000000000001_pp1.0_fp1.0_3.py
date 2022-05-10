import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)

#Initialization
if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/cctv"):
    os.makedirs("data/cctv")

if not os.path.exists("data/snapshot"):
    os.makedirs("data/snapshot")

if not os.path.exists("data/snapshot/cctv"):
    os.makedirs("data/snapshot/cctv")

if not os.path.exists("data/snapshot/cctv/upload"):
    os.makedirs("data/snapshot/cctv/upload")

if not os.path.exists("data/snapshot/cctv/analysis"):
    os.makedirs("data/snapshot/cctv/analysis")

__custom_error_code__ = {"CP_ERR_ALREADY_STARTED": -10,
                         "CP_ERR
