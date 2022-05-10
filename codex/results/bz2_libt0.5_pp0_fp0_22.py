import bz2
bz2.BZ2File(filename, 'wb').write(data)

# a file-like object
import bz2
f = bz2.BZ2File(filename, 'wb')
f.write(data)
f.close()

# compress a file
import bz2
input = open('file.txt', 'rb')
s = input.read()
input.close()
output = bz2.BZ2File('file.txt.bz2', 'wb')
output.write(s)
output.close()

# decompress a file
import bz2
input = bz2.BZ2File('file.txt.bz2', 'rb')
s = input.read()
input.close()
output = open('file.txt', 'wb')
output.write(s)
output.close()

# compress a string
import bz2
compressed = bz2.compress(data)

# decompress a string
import bz2
decompressed = bz2.decompress(compressed)

# compress a
