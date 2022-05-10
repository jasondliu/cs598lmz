import mmap
# Test mmap.mmap_size()

def test_mmap_size():
    m1 = mmap.mmap(0, 1)
    assert m1.size() == 1
    assert m1.file_size() == 1

def test_mmap_size_large():
    m1 = mmap.mmap(0, 0xFFFFFFFF)
    assert m1.size() == 0xFFFFFFFF
    assert m1.file_size() == 0xFFFFFFFF

def test_mmap_copy():
    m1 = mmap.mmap(0, 1)
    m2 = m1.copy()
    assert m1.size() == 1
    assert m2.size() == 1
    assert m1.tell() == 0
    assert m2.tell() == 0
    assert m1.file_size() == 1
    assert m2.file_size() == 1

    assert m2.find(b"") == 0
    assert m2.rfind(b"") == 0

def test_mmap_start_stop():
    m1 = mmap.mm
