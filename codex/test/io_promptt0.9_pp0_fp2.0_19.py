import io
# Test io.RawIOBase method
io.RawIOBase()
# Test io.BufferedIOBase method
io.BufferedIOBase()
# Test io.TextIOBase method
io.TextIOBase()
# Test io.IOBase method
io.IOBase()
# Test io.FileIO method...
try:
    io.FileIO()
except TypeError:
    pass

# Subprocess module.
import subprocess
# Test subprocess.STARTUPINFO method
