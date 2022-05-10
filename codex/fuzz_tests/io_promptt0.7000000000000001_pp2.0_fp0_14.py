import io
# Test io.RawIOBase
subprocess.Popen("ls", stdout=io.RawIOBase())
