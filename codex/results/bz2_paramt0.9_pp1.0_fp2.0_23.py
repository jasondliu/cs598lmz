from bz2 import BZ2Decompressor
BZ2Decompressor
# need this BZ2D compressor so that we can compress the data
import bz2
bz2.BZ2Compressor
import numpy as np
d=np.random.uniform(0,1, (1000, 1000))
d.shape
%timeit -n 1000 d.reshape((-1, 1))
%pylab inline
import numpy as np

# generate some random numbers, a 1000x1000 array with values between 0 and 1
d = np.random.uniform(0, 1, (1000, 1000))

print(d.shape, d.dtype)
%timeit -n 20 d.reshape((-1, 1))

# plot d as an image
imshow(d, cmap='gray');

# reshape d to 2D vector, with 1000 rows and 1 column
# this way `size` returns 1000
d2 = d.reshape((-1, 1))
print(d2.shape, d2.dtype, d2.size)

# reshape d to 1D vector, with 1000 elements
# this way `size`
