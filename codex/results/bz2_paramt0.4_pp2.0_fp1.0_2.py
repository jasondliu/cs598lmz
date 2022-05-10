from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# the data is a base64 encoded string
from base64 import b64decode
b64decode(data)

# the data is a string of numbers
# the string is split into a list of numbers
# the numbers are converted to integers
# the list is converted to a numpy array
# the array is reshaped into a 2D array
data = np.array(list(map(int, data.split()))).reshape((100, 100))

# the first row of the data is printed
print(data[0])

# the data is summed along the columns
# the sum is printed
print(data.sum(axis=0))

# the data is summed along the rows
# the sum is printed
print(data.sum(axis=1))
