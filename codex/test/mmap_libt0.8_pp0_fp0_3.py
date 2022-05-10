import mmap
# with open('/root/workspace/myblog/myblog/tests.py', 'rb', 0) as file:  # Python 3
#     mem = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
#     string = mem.readline()
#     print(string)

#
# import StringIO, mmap
# # Write a string to a buffer using StringIO
# output = StringIO.StringIO()
# output.write('This goes into the buffer. ')
# print 'And so does this.'
#
# # Retrieve the value written
# # ...
# print output.getvalue()

# output = StringIO.StringIO()
# output.write('First line.\n')
# print >>output, 'Second line.'
#
# # Retrieve file contents -- this will be
# # 'First line.\nSecond line.\n'
# contents = output.getvalue()
#
# # Close object and discard memory buffer --
# # .getvalue() will now raise an exception.
# output.
