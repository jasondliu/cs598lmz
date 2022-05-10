import ctypes
ctypes.cast(map_adr, ctypes.POINTER(ctypes.c_ubyte))[:32 * 1024 * 1024] = bytes
</code>
This works well, but I would like to avoid to copy the whole memory region if I want to update only few bytes.
I can use <code>mmap</code> to create a memory map on an arbitrary file:
<code>with open(...) as f:
    mm = mmap.mmap(f.fileno(), length=size, access=mmap.ACCESS_WRITE)
</code>
Is there a way to use <code>mmap</code> on a memory region?
EDIT:
I found a solution, but it's very ugly:
<code>def map_adr_to_file(adr, size):

    memmap = mmap.mmap(-1, size)
    memmap[:] = ctypes.string_at(adr, size)
    return memmap


def unmap_file_to_adr(memmap, adr, size):

    ctypes.memmove(adr, memmap, size)
    memmap
