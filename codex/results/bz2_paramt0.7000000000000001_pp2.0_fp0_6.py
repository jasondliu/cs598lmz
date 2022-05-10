from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f.read())

# Make sure to close the file after use
f.close()

# This function returns a file-like object
def myfunc():
    return open('myfile.txt')


# The file-like object is an iterator
for line in myfunc():
    print(line)

# It must be explicity closed
myfunc().close()
# To automatically close the file
with myfunc() as f:
    print(f.read())

# Since the with keyword automatically closes the file, there is no need to call f.close()
# The file is closed even if the code raises an exception
f = open('myfile.txt')

try:
    print(f.read())
finally:
    f.close()

# This is the equivalent of the above code
with open('myfile.txt') as f:
    print(f.read())

# The with keyword is a context manager. It can also be used with other objects in a similar way
with open('myfile.txt') as f:
    with open('myfile2.txt
