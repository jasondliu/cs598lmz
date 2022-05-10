import select
# Test select.select() for the write-end of a pipe

import select, os, time

rd, wr = os.pipe()

print "Testing blocking case"
print '  calling select([], [%d], [], -1)' % wr
print '   ',
r, w, e = select.select([], [wr], [], -1)
print '   return: r=%s w=%s e=%s' % (r, w, e)
print

print "Testing non-blocking case"
print '  calling select([], [%d], [], 1)' % wr
print '   ',
r, w, e = select.select([], [wr], [], 1)
print '   return: r=%s w=%s e=%s' % (r, w, e)
print

# OK, now the write-end is ready to be written, so let's write

bytes_written = os.write(wr, b"testing")
print("wrote %d bytes" % bytes_written)
first_line = time.asctime()

print("waiting
