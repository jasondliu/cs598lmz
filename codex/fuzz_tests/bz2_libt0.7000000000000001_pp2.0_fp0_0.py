import bz2
bz2.BZ2File("./test.bz2",'r').read()

# Here we are reading and writing compressed files directly
# instead of using a decompressing file wrapper

print '\n\n'

import gzip
f = gzip.open('../test.txt.gz','rb')
file_content = f.read()
f.close()

print file_content
print '\n\n'

import gzip
f = gzip.open('../test.txt.gz','wb')
f.write('Thank you for compressing with us!')
f.close()

print f.read()
print '\n\n'

# This is an example of how to use the StringIO function
# to capture the output of a function and write it to a file

import cStringIO

output = cStringIO.StringIO()
output.write('This goes into the buffer. ')
output.write('And so does this.')

# Retrieve the value written
print output.getvalue()

output.close()

# This example shows how
