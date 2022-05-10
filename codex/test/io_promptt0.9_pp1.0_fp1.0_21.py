import io
# Test io.RawIOBase interface
class BytesIOWrapper(io.RawIOBase):

    def __init__(self, bytes):
        self.read_stack = [memoryview(bytes)]

    def readinto(self, buf):
        current_view = self.read_stack[-1]
        l = len(buf)
        # Test for closedness:
        self.read_stack[-1:]
        if len(current_view) < l:
            ioview = current_view

            class Trap:
                def readinto(self):
                    self.readinto_called = True
                    return 0

            new_buf = Trap()
            result = ioview.tobytes(new_buf)
            assert new_buf.readinto_called
            if result:
                buf[:result] = ioview[:result]
            return result
        result = l
        buf[:l] = current_view[:l]
        current_view = current_view[l:]
        if len(current_view) == 0:
            self.read_stack.pop()

