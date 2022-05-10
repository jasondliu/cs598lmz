import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'a'*n

try:
    f = open('/dev/stdout', 'w')
except IOError as err:
    print("I/O error: {0}".format(err))
else:
    print('File opened successfully')
    f.close()

print('\n')

#
#
#
#
#

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
print("Softspace flag : ", fo.softspace)

# Close opend file
fo.close()

print('\n')

#
#
#
#
#

#!/usr/bin/python

# Open a file
fo = open("foo.txt", "wb")
print("Name of the file: ", fo.name)

# Close opend file
fo.close
