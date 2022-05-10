import select
# Test select.select() on a regular file.
# This should not block at all.

import os
import select

file_name = os.tmpnam()
f = open(file_name, "w")
f.write("x" * 1024)
f.close()

f = open(file_name, "r")
r, w, e = select.select([f], [], [])
print(r, w, e)
