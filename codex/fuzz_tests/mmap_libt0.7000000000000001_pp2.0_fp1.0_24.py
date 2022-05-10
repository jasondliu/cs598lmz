import mmap
import re

def meminfo():
    map = mmap.mmap(0, 4096, 'meminfo')
    map.seek(0)
    return map.readline()

def memfmt(size):
    if size >= 1048576.0:
        return '%4.2f GB' % (size / 1048576.0)
    elif size >= 1024.0:
        return '%4.2f MB' % (size / 1024.0)
    else:
        return '%4.2f KB' % size

def get_meminfo():
    m = meminfo()
    mem = {}
    mem['total'] = int(re.sub('.*MemTotal:\s*(\d*).*', '\\1', m))
    mem['free'] = int(re.sub('.*MemFree:\s*(\d*).*', '\\1', m))
    mem['cached'] = int(re.sub('.*Cached:\s*(\d*).*', '\\1', m))
    mem['buffers'] =
