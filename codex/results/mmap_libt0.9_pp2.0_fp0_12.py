import mmap
import os

desc = """
This script will use a page table of type PFN to PTE to
scan a specified memory file for a page table.

Usage is:
mmap_pgd_test.py [options] <input_file>

Options are:
    -h, --help          Print this help message
    -a, --addr          Start address to look for PT (default 0x0)
    -s, --size          How much to read (default is 0x1000)
    -o, --offset        Offset to start of PT file (default 0)
    -b, --base          Base Address (default 0x0)

examples:
    ./mmap_pgd_test.py --offset=0x200000 --base=0x80000000 --addr=0x1000 --size=0x1000 mem.dmp
    ./mmap_pgd_test.py --addr=0x1000 mem.dmp

"""

UNALLOCATED_MEMORY = 0xffffffff # page is not allocated
END_OF_MEMORY      = 0x0        #
