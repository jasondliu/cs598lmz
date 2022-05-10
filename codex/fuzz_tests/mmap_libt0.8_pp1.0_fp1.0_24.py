import mmap
import errno

# Importing system symbols for the unmap() function
SYMBOL_TABLE = None
def load_system_symbols():
    global SYMBOL_TABLE
    with open('/proc/kallsyms', 'rt') as f:
        SYMBOL_TABLE = dict((s, addr) for (addr, t, s) in [line.split() for line in f.readlines()])
load_system_symbols()

# Paths to use
BASE_PATH = '/sys/kernel/debug/tracing'
DIR_PATH = os.path.join(BASE_PATH, 'events/mmc')
FILE_PATH = os.path.join(DIR_PATH, 'mmc_blk_rw_start')

# Sizes to malloc()
TRACE_HEADER_SIZE = 0x1000
TRACE_MAPPING_SIZE = 0x1000

# Addresses for the system trace
TRACE_BASE = 0xffffffc000000000
TRACE_PAGE_OFFSET = 0x0000000000100000

#
