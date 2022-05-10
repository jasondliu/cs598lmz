import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

def warn(msg):
    print("[WARN]", msg)

def error(msg):
    print("[ERROR]", msg)

def debug(msg):
    print("[DEBUG]", msg)

def info(msg):
    print("[INFO]", msg)

def setup_logger(level):
    if level == "debug":
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    elif level == "info":
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    elif level == "warn":
        logging.basicConfig(level=logging.WARN, format='%(asctime)s - %(levelname)s - %(message)s')
    elif level == "error":
        logging.basicConfig
