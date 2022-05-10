import io
# Test io.RawIOBase
try:
    io.RawIOBase.close
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedIOBase
try:
    io.BufferedIOBase.close
except AttributeError:
    print('SKIP')
    raise SystemExit


class MyRaw(io.RawIOBase):
    def close(self):
        print("raw close")


class MyBuffered(io.BufferedIOBase):
    def close(self):
        print("buffered close")


m = MyRaw()
m.close()
m = MyBuffered()
m.close()
