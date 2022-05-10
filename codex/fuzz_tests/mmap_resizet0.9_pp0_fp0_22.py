import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    f.truncate()
    a = m[:]
"""
        )
        script = self.make_test_prog(source)
        # Mypy thinks truncate() might return None here.
        f = create_mypyc_tmp(name="truncate", source=script, flags=["--no-site-packages"])
        mmap = pytest.importorskip("mmap")
        assert f(mapping="const", access="const")
        assert f(mapping="const", access="const")
        assert len(self.out) == 2
        assert self.out == "b''\nb''\n"


def test_mypyc_command_line_file_ok() -> None:
    """Make sure a file flag is correctly handled."""
    f =
