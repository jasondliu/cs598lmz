import select
# Test select.select

# Create a pipe with two file descriptors.
r, w = os.pipe()

# Pre-condition: neither fd is ready.
read_fds, _, _ = select.select([r], [], [], 0.0)
assert not read_fds
write_fds, _, _ = select.select([], [w], [], 0.0)
assert not write_fds

# Write to the pipe.
os.write(w, b'42')
os.close(w)

# Post-condition: the read fd is ready.
read_fds, _, _ = select.select([r], [], [], 0.0)
assert read_fds == [r]
write_fds, _, _ = select.select([], [w], [], 0.0)
assert not write_fds

# Read the result.
result = os.read(r, 1024)
assert result == b'42'
os.close(r)

# Post-condition: neither fd is ready.
