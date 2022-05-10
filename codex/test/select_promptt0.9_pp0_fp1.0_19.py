import select
# Test select.select() for the write-end of a pipe

import select, os, time

rd, wr = os.pipe()

