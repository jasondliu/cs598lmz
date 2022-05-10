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
            try:
                with open("{}/resource0".format(path),'r') as f:
                    resource0 = f.read()
                    m = re.match("(?:0x)*([0-9a-fA-F]+)", resource0)
                    if m:
                        mem_base = int(m.group(1),16)
                with open("{}/resource1".format(path),'r') as f:
                    resource1 = f.read()
                    m = re.match("(?:0x)*([0-9a-fA-F]+)", resource1)
                    if
