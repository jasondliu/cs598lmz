import mmap, time, struct

# struct_format = '<' + 'Lf' * 8
# struct_format = '<' + 'L' * 10
struct_format = '<' + 'L' * 11
buffer_size = struct.calcsize(struct_format)

def main():
    fd = os.open('/tmp/test_mem.mmap', os.O_RDONLY)
    
    while True:
        buf = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)
        # data = struct.unpack(struct_format, buf.read(buffer_size))
        data = struct.unpack(struct_format, buf.read(buffer_size))
        # print ', '.join(['0x%02x' % ord(c) for c in buf.read(buffer_size)])
        # print data
        print data
        buf.close()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
