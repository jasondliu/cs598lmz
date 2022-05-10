import ctypes
ctypes.cdll.LoadLibrary("lib/libgsl.so")

# Setup environment and import libraries
import gsl, numpy, sys, os
from numpy import array

# Force python to print entire array
numpy.set_printoptions(threshold=numpy.nan)

# Initialize counters and flags
i = 1
j = 0

# Check if the required directories exist and create them if not
if not os.path.exists("figures"):
	os.makedirs("figures")
if not os.path.exists("temp"):
	os.makedirs("temp")

# Read data from the input file and load them into variables
x = gsl.gsl_vector_alloc(len(sys.argv)-1)
y = gsl.gsl_vector_alloc(len(sys.argv)-1)
for arg in sys.argv[1:]:
	gsl.gsl_vector_set(x,j,float(i))
	gsl.gsl_vector_set(y,j,float(arg))
	
