import mmap
import struct

# process_id = '660'
# process_id = '14112'
process_id = '15184'

def read_float(address):
    mem_file = open("/proc/{0}/mem".format(process_id), "rb")
    mem = mmap.mmap(mem_file.fileno(), 4, mmap.MAP_SHARED, mmap.PROT_READ)
    mem.seek(address)
    return struct.unpack('f', mem.read(4))[0]

def read_int(address):
    mem_file = open("/proc/{0}/mem".format(process_id), "rb")
    mem = mmap.mmap(mem_file.fileno(), 4, mmap.MAP_SHARED, mmap.PROT_READ)
    mem.seek(address)
    return struct.unpack('i', mem.read(4))[0]

def read_char(address):
    mem_file = open("/proc/{0}/mem".format
