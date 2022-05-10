import mmap
import struct

def find_camera_module(mem_prefix):
    reg_path = "/sys/devices"
    dir_iter = os.walk(reg_path)
    regiter = (x[0] for x in dir_iter)
    while mem_prefix:
        try:
            path = next(regiter)
        except StopIteration:
            return None
        if path.startswith(mem_prefix):
            mem_base = 0
