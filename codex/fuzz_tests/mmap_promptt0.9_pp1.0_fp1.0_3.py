import mmap
# Test mmap.mmap() under win64
class test_mmap_win64(unittest.TestCase):
    def test_init_0(self):
        # To fit in memory
        n = 10*1024
        m=mmap.mmap(0,n)
        for i in range(n): m[i]='\x00'
        for i in range(n): self.assertEqual(m[i],'\x00')
        for i in range(n): m[i]='x'
        for i in range(n): self.assertEqual(m[i],'x')
        m.close()

    def test_init_0_access(self):
        # To fit in memory
        n = 10*1024
        m=mmap.mmap(0,n,access=mmap.ACCESS_READ)
        m.close()

    def test_init_0_offset(self):
        # To fit in memory
        n = 10*1024
        offset = 1
        m=mmap.mmap(0,n,offset=offset)
       
