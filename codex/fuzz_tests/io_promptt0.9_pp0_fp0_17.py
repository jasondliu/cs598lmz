import io
# Test io.RawIOBase
wrapper = io.BufferedReader(io.BytesIO(b"abcde"))
underlying = wrapper.raw
assert isinstance(underlying, io.BytesIO)
assert underlying.readinto(bytearray(2)) == 2
assert underlying.readinto(bytearray(4)) == 3
print(underlying.tobytes())

# Test io.BufferedIOBase
class CustomIO(io.RawIOBase):
    def readinto(self, b):
        return 0
base = CustomIO()
assert not isinstance(base, io.BufferedIOBase)
wrapper = io.BufferedReader(base)
assert isinstance(wrapper, io.BufferedIOBase)

# Test __dict__ on a closed socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
assert not soc.closed
soc.close()
assert soc.closed
try:
    soc.__dict__
except ValueError:
    pass
finally:
    try:
        soc.detach()
    except:
        pass

# Test
