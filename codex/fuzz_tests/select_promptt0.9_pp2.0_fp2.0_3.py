import select
# Test select.select for bad parameters.
import sys
if sys.platform == 'win32':
    raise TestSkipped('Windows select() has "weird" semantics.')
select.select([], [], [], 0.0)
select.select([], [], [], -1.0)
try:
    select.select([], [], [], -1.0 + sys.float_info.min)
except OverflowError:
    pass
try:
    select.select([], [], [], None)
except TypeError:
    pass

# Verify that select, poll and epoll return select.POLLNVAL for:
# - file descriptors that are never opened
# - file descriptors that are closed
#
# These file descriptors are valid file descriptors, but select still needs to
# return POLLNVAL and not raise an unhandled signal.

# fdopen
# Check fdopen with file descriptor of a file opened in append mode.
tmp = tempfile.TemporaryFile()
t = open(tmp.fileno(), 'a')
try:
    t.write('abc\n
