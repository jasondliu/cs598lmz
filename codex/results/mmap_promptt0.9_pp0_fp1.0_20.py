import mmap
# Test mmap.mmap for page-aligned memory
print(mmap.mmap.PAGESIZE, mmap.mmap.ALLOCATIONGRANULARITY)
print(mmap.mmap(0, mmap.mmap.ALLOCATIONGRANULARITY))
</code>
I tried it on my Windows 10 machine and it worked fine.  If there is a difference between the operating systems, it must be related to something they do differently when mapping pages containing executable code; I doubt it would be related to memory alignment.

