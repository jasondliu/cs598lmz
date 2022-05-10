import mmap
import errno

# Importing system symbols for the unmap() function
SYMBOL_TABLE = None
def load_system_symbols():
    global SYMBOL_TABLE
    with open('/proc/kallsyms', 'rt') as f:
        SYMBOL_TABLE = dict((s, addr) for (addr, t, s) in [line.split() for line in f.readlines()])
