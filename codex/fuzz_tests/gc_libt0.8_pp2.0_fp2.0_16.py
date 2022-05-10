import gc, weakref
import heapq # for pq-sort

# constants
_maxInt = sys.maxsize
_minInt = -sys.maxsize - 1
_defaultTol = 0.0001
_defaultInterval = [0, 1]

# The data structures in this file:
#
# Allocation metadata:
#   _RawBlock is part of the allocation metadata for a PyPy object,
#   and records where it is located, if at all.
#
# A page (a unit of allocation):
#   A Page is a Unit of allocation, which is 1Mb, the minimum unit
#   that we can allocate from the mmap.
#
#   Each page is a doubly linked list of blocks, linked by
#   a doubly linked list of _RawBlocks.
#   when a block is freed, it is appended to the list of blocks
#   contained in the page.
#   When a page is full, a new page is allocated.
#
#   A Page is allocated from the mmap by the _PageAllocator.
#
# A block-list (list of free blocks
