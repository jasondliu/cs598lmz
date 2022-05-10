import mmap
# Test mmap.mmap against bigbuffer.charbuffer
from bigbuffer import bigbuffer
from bigbuffer import shm

# Linear writing, continuous reading

class TestMmapStressLinear(unittest.TestCase):
    
    def setUp(self):
        mmap.NODE = "/mmap-stress-shm-%d" % self.id()
        mmap.PERM = os.O_RDWR | os.O_CREAT | os.O_TRUNC
        mmap.FD = -1
        try:
            os.unlink(mmap.NODE)
        except OSError:
            pass
        self.basemap = 1024
        self.itemcount = 1024 * 4
        self.chunksize = self.basemap // self.itemcount
        self.map = mmap.mmap(self.basemap)
        self.chunks = [self.chunksize for x in range(self.itemcount)]
        self.chunks[-1] += self.basemap % self.itemcount
    
    def tearDown(self
