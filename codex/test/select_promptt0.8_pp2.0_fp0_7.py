import select
# Test select.select for stdin, stdout, and pipe, then close pipe.
pipe_r, pipe_w = os.pipe()
r, w, x = select.select([0, pipe_r], [1, pipe_w], [])

# write twice to the pipe
os.write(pipe_w, b'spam')
os.write(pipe_w, b'eggs')

# read twice from the pipe
try:
    os.read(pipe_r, 4)
except BlockingIOError:
    pass
assert os.read(pipe_r, 4) == b'eggs'

# Close the write end.  The read end should still be readable.
os.close(pipe_w)
try:
    os.read(pipe_r, 4)
except BlockingIOError:
    pass
assert os.read(pipe_r, 4) == b''
os.close(pipe_r)

