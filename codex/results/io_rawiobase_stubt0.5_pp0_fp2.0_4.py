import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b'\x00' * n

def test_file_read_write(monkeypatch):
    monkeypatch.setattr(io, 'open', lambda *args, **kwargs: File())
    assert read_file('/dev/null') == b''
    assert read_file('/dev/null', 1) == b'\x00'
    assert read_file('/dev/null', 2) == b'\x00' * 2
    assert read_file('/dev/null', 3) == b'\x00' * 3
    assert read_file('/dev/null', 4) == b'\x00' * 4
    assert read_file('/dev/null', 5) == b'\x00' * 5
    assert read_file('/dev/null', 6) == b'\x00' * 6
    assert read_file('/dev/null', 7) == b'\x00' * 7
    assert read_file('/dev/null', 8) == b'\x00' * 8
