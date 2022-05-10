import _struct

# Return msr value
    
def read(core_id, msr_id):
    try:
        f = os.open("/dev/cpu/%d/msr" % core_id, os.O_RDONLY)
        out = os.lseek(f, msr_id, os.SEEK_SET)
        out = os.read(f, 8)
    finally:
        os.close(f)
    return _struct.unpack("<Q", out)[0]


# Write msr value
    
def write(core_id, msr_id, value):
    try:
        f = os.open("/dev/cpu/%d/msr" % core_id, os.O_WRONLY)
        out = os.lseek(f, msr_id, os.SEEK_SET)
        out = os.write(f, _struct.pack("<Q", value) )
    finally:
        os.close(f)
    return True

def hw_info(cores):
    '
