import mmap
# Test mmap.mmap.close_fd
import subprocess

with open('/dev/zero', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
m.close_fd()

# This line should not raise OSError
subprocess.check_output(['ls', '/dev/zero'])
