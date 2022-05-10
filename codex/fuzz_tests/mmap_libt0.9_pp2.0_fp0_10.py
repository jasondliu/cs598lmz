import mmap
import re
import codecs

def readFile(filename):
    import sys
    try:
        f = codecs.open(filename, encoding='utf-8')
    except IOError:
        e = sys.exc_info()[1]
        print(e)
        sys.exit()

    str = f.readlines()
    lines = []
    for line in str:
        lines.append(line)
    f.close()
    return lines


def psize(size):
    size = float(size) / 1024. # Convert to KiB
    if size < 1024.:
        return "%.2f KiB" % size
    size = size / 1024. # Convert to MiB
    if size < 1024.:
        return "%.2f MiB" % size
    size = size / 1024. # Convert to GiB
    return "%.2f GiB" % size

total_size = 0.

lines1 = readFile("/proc/swaps")
for line in lines1:
    m = re.search(r'^(\S+)\s
