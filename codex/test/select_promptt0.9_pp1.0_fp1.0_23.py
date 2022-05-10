import select
# Test select.select() with a custom FD_SETSIZE.
from test.support import big_FD_SETSIZE
from test.support import socket_helper
old_size = select.FD_SETSIZE
select.FD_SETSIZE = big_FD_SETSIZE
try:
    s, reads, _, _ = socket_helper.socket_helper()
    s, writes, _, _ = socket_helper.socket_helper()
    result = select.select(reads, writes, [], 0)
finally:
    select.FD_SETSIZE = old_size
