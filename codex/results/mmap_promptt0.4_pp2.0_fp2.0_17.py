import mmap
# Test mmap.mmap
import mmap

def test_mmap():
    mm = mmap.mmap(-1, 1024)
    mm[0] = 'a'
    assert mm[0] == 'a'
    mm.close()

# Test mmap.mmap.find
import mmap

def test_mmap_find():
    mm = mmap.mmap(-1, 1024)
    mm[0] = 'a'
    mm[1] = 'b'
    mm[2] = 'c'
    mm[3] = 'd'
    mm[4] = 'e'
    mm[5] = 'f'
    mm[6] = 'g'
    mm[7] = 'h'
    mm[8] = 'i'
    mm[9] = 'j'
    mm[10] = 'k'
    mm[11] = 'l'
    mm[12] = 'm'
    mm[13] = 'n'
    mm[14] = 'o'
    mm[15] = 'p'
    mm
