import mmap
# Test mmap.mmap(0,1).move(1,0,1) with various combinations of
# access=mmap.ACCESS_*

def do_move(access):
    m = mmap.mmap(0, 1, access=access)
    m.move(1, 0, 1)
    m.close()
