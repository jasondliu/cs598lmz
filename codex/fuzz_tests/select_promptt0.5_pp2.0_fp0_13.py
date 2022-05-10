import select
# Test select.select() on a pipe

import os
import select
import time

pipe_read, pipe_write = os.pipe()

# select() should return immediately, even though the pipe is empty
select.select([pipe_read], [], [], 0.0)

# select() should return immediately, even though the pipe is empty
select.select([pipe_read], [], [], 0.0)

# select() should block until the pipe is written to
select.select([pipe_read], [], [], None)

# select() should return immediately, since the pipe is readable
select.select([pipe_read], [], [], 0.0)

# select() should block until the pipe is written to
select.select([pipe_read], [], [], None)

# select() should return immediately, even though the pipe is empty
select.select([pipe_read], [], [], 0.0)

# select() should return immediately, even though the pipe is empty
select.select([pipe_read], [], [], 0.0)

# select() should block until the pipe is written
