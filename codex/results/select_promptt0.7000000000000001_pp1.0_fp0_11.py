import select
# Test select.select()
print 'Testing select.select'

# This should be a socket that we can write to, but
# not read from.
import sys
if sys.platform[:3] == 'win':
    print '  This test does not work on windows'
    sys.exit(0)

write_only = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
write_only.connect(('www.python.org', 80))
write_only.setblocking(0)

# This should be a socket that we can read from, but
# not write to.
read_only = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
read_only.connect(('www.python.org', 80))
read_only.setblocking(0)

# try writing to the read-only socket.
try:
    write_only.send('GET /\n')
except socket.error, why:
    if why[0] != errno.EWOULDBLOCK:
        raise
else:
    raise RuntimeError, "s
