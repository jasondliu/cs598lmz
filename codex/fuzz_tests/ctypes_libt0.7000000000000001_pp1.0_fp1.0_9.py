import ctypes
ctypes.cdll.LoadLibrary("double")
lib = ctypes.cdll.LoadLibrary("double")

# Test with 1,2,3,4
print lib.double(1)
print lib.double(2)
print lib.double(3)
print lib.double(4)

#here is the output
2
4
6
8

#This works as expected, but if I try to call the function from an array, I get a segfault.

# Create an array of length 4
import numpy as np
a = np.array([1,2,3,4])

# Test with the array
print lib.double(a)

# Here is the output
0
Segmentation fault

# I have also tried this with an array of length 1, and
# still get the segfault.

# Create an array of length 1
import numpy as np
a = np.array([1])

# Test with the array
print lib.double(a)

# Here is the output
0
Segmentation fault
</code>
I am not sure why
