import ctypes
# Test ctypes.CField definition

PONDROW = ctypes.c_int
PONDCELL = ctypes.c_int

class world_t(ctypes.Structure):
    _fields_ = [ 
                ("pond_size_row", PONDROW),
                ("pond_size_column", PONDROW),
                ("pond_size_flock", PONDROW),
                ("pond", PONDCELL * 600),
                ]

if __name__ == '__main__':
    import random
    import pprint
    pprint.pprint(world_t.pond_size_row)
    pprint.pprint(world_t.pond_size_column)
    pprint.pprint(world_t.pond_size_flock)
    world = world_t()
    world.pond = [random.randrange(10) for i in xrange(3600)]
    pprint.pprint(world.pond[::350])
