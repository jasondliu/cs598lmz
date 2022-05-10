import ctypes
ctypes.CDLL('libomp.dylib')
os.environ["OMP_NUM_THREADS"] = "3" # export OMP_NUM_THREADS=4
os.environ["OPENBLAS_NUM_THREADS"] = "3" # export OPENBLAS_NUM_THREADS=4 
os.environ["MKL_NUM_THREADS"] = "3" # export MKL_NUM_THREADS=6
os.environ["VECLIB_MAXIMUM_THREADS"] = "3" # export VECLIB_MAXIMUM_THREADS=4
os.environ["NUMEXPR_NUM_THREADS"] = "3" # export NUMEXPR_NUM_THREADS=6
 
#set & print Environment Variables
logging.debug("Python Version: %s", sys.version)
logging.debug("Pandas Version: %s", pd.__version__)
logging.debug("Sklearn Version: %s", sklearn.__version__)
logging.debug("Numpy Version: %s", np
