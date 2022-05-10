import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# Define the functions of the libraries
polyfit = numpy.polyfit
linspace = numpy.linspace

# Define root path of Python wrapper
ROOT_PATH = os.path.dirname(__file__)

# Define the location of the libraries
LIB_FOLDER = ospathjoin(ROOT_PATH, 'lib')

# Define the suffix of the library to import. If you are running a Windows
# machine with a 32-bit version of Python, you must use '.dll'. If you are
# running a 64-bit version of Python, you must use '.dll'.
LIB_SUFFIX = '.dll'

# Define the name of the library to import
LIB_NAME = 'polyfit' + LIB_SUFFIX

# Define the full path of the library to import
LIB_PATH = ospathjoin(LIB_FOLDER, LIB_NAME)

# Import the library
try:
    LIB = ctypes.CDLL(LIB_PATH)
except:
    msg = 'Could not load the library
