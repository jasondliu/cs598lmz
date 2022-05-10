import select
# Test select.select performance with a large number of file descriptors.

# See also: http://bugs.python.org/issue1026

# On Linux and OS X, this runs about 10x faster than Python 2.4.
# It is limited by the speed of poll() and select().

numfds = 1024
