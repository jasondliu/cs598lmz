import select
# Test select.select using stdin file descriptor, and a timeout.

import sys

invalid = [0, 1, 2]
read_r, write_w, err_e = select.select([sys.stdin], [], invalid, 1)
print (read_r, write_w, err_e)

invalid = [0, 1, 2]
read_r, write_w, err_e = select.select([sys.stdin], [], invalid, 1.0)
print (read_r, write_w, err_e)

invalid = [0, 1, 2]
read_r, write_w, err_e = select.select([sys.stdin], [], invalid, -1.0)
print (read_r, write_w, err_e)

invalid = [0, 1, 2]
read_r, write_w, err_e = select.select([sys.stdin], [], invalid, None)
print (read_r, write_w, err_e)

invalid = [0, 1, 2]
read_r
