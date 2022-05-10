import bz2
bz2_compress = bz2.compress
bz2_decompress = bz2.decompress

# Define the C binding file
ffi = FFI()
ffi.cdef("""

typedef struct {
  uint64_t offset;
  size_t nbytes;
} BZ2CompressedChunkMeta;

typedef struct {
  size_t nchunks;
  BZ2CompressedChunkMeta* chunks;
} BZ2CompressedChunkMetaArray;

typedef struct {
  uint64_t offset;
  size_t nbytes;
} CompressedChunkMeta;

typedef struct {
  int32_t nchunks;
  CompressedChunkMeta* chunks;
} CompressedChunkMetaArray;

/* Returns -1 on failure, 0 on success */
int compress_fixed_chunk_size(uint8_t* target, size_t tlen, uint8_t* source, size_t slen,
                              size_t chunk_size, BZ2
