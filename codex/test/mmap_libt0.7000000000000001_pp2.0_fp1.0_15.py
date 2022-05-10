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
