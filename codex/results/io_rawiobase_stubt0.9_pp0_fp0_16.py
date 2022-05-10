import io
class File(io.RawIOBase):
    def readline(self):
        return b'line\n'


def test_readlines():
    assert f.readlines() == ['line\n', 'line\n']


def test_basic_iterator():
    assert list(iter(f)) == ['line\n', 'line\n']


def test_iterator_context():
     with pytest.raises(ValueError):
        for line in f:
            f.readline()
