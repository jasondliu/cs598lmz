import mmap
# Test mmap.mmap.write
with open("map_write_file", "w+b") as f:
    f.write(b"01234")
    with mmap.mmap(f.fileno(), 0) as m:
        with pytest.raises(TypeError):
            m.write(1)
        with pytest.raises(ValueError):
            m.write(b"abcde")
        m.write(b"abc")
        assert m[:5] == b"01abc"


@with_file_contents(b"01234")
def test_mmap_write_bytes(filename):
    with mmap.mmap(filename, 0) as m:
        m.write(b"abc")
        assert m[:5] == b"01abc"


@with_file_contents(b"01234")
def test_mmap_write_bytearray(filename):
    with mmap.mmap(filename, 0) as m:
        m.write(bytearray(b"abc"))
        assert m[:5]
