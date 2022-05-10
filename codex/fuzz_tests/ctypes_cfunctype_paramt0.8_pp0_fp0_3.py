import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# Function to generate random numbers
def random1(x=0):
    ctr = 0
    while True:
        x = (123456789 + x * 876543219) % 4294967296
        ctr += 1
        yield x / 4294967296.0

# Original numbers
original = list(random1(123456789))

# Define the function
def random_number(x=0):
    x = (123456789 + x * 876543219) % 4294967296
    return x / 4294967296.0

# Wrap the function
f = FUNTYPE(random_number)
# Create an instance
lib = ctypes.CDLL('')
lib.my_function.argtypes = [FUNTYPE]
lib.my_function.restype = ctypes.c_double

# Test the function
a = lib.my_function(f)
print(a)

# Generate the sequence
result = []
for i in range(1, len(original
