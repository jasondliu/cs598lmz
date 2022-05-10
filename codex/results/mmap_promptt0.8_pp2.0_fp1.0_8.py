import mmap
# Test mmap.mmap and mmap.PAGEEAK to read every N lines and collect
# every N lines in a file (in a memory-efficient manner)

def fetch_para(file_path, i):
    with open(file_path, 'r+') as f:
        mm = mmap.mmap(f.fileno(), 0)
        mm.seek(0)
        line = mm.readline()
        pos = mm.tell()
        count = 0
        while line:
            if i == count:
                pos -= mm.tell()
                return mm[pos:pos+mm.tell()]
            else:
                pos -= mm.tell()
                mm.seek(mm.tell() + mm.PAGESIZE)
                mm.readline()
                count += 1


# Test mmap.mmap and mmap.PAGEEAK to read every N lines and collect
# every N lines in a file (in a memory-efficient manner)

def fetch_lines(file_path, i, lines_per_fetch):
    with open(file_path, 'r+
