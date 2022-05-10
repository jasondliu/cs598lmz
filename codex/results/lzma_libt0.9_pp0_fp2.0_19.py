import lzma
lzma.LZMA_FORMAT_AUTO, lzma.LZMA_MEMLIMIT

MAP_SHARED = 0x01
PROT_READ = 0x01
PROT_WRITE = 0x02
assert mmap.ACCESS_READ == PROT_READ and mmap.ACCESS_WRITE == PROT_WRITE

vec_types = VectorType, RangeType, ListComp, ListCompFor
typing_extensions = inspect.getmembers(typing, lambda obj: isinstance(obj, TypeVar))


class WriteCache:

    def __init__(self, *, compresslevel=compresslevel):
        self.compresslevel = compresslevel
        self._os = _compresslevel_to_string(compresslevel)
        self.uncompressed = io.BytesIO()
        self.buffered = io.BufferedIOBase(self.uncompressed)
        self.records = []

    def write(self, record):
        self.buffered.write(serialize(record)) # includes pickling overhead
        self.records.
