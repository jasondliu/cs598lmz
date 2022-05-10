import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        pass
    def read(self, *args, **kwargs):
        return b'123456789'
    def seek(self, *args, **kwargs):
        pass
    def close(self):
        pass

class FakeFileSystem(object):
    def __init__(self):
        self.files_to_return = []
    def open(self, *args, **kwargs):
        return self.files_to_return.pop(0)

def test_read_from_file_returns_a_base_file_object():
    file_system = FakeFileSystem()
    file_system.files_to_return = [File()]
    assert isinstance(read_from_file('data.txt', file_system), File)
    assert not file_system.files_to_return

def test_read_from_file_when_files_to_return_is_empty_throws_exception():
    file_system = FakeFileSystem()
    with pytest.
