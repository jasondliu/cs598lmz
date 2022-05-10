import mmap
import os
import re
import sys

def get_memory_stats():
    pid = str(os.getpid())
    with open('/proc/{}/status'.format(pid)) as f:
        data = f.read()
    return {
        'vms': int(re.search(r'VmSize:\s*(\d+) kB', data).group(1)) * 1024,
        'rss': int(re.search(r'VmRSS:\s*(\d+) kB', data).group(1)) * 1024,
    }

# Get the input and output filenames from the command line
in_filename = sys.argv[1]

# Open the input file as a binary stream
in_file = open(in_filename, 'rb')

# Create a memory map for the input file
map_file = mmap.mmap(in_file.fileno(), 0, prot=mmap.PROT_READ)

# Find the start of the second sequence
start = map_file.find(b'\n>') + 1

