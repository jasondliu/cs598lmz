import lzma
lzma_path('../liblzma/src/liblzma')
import lzma
import cffi

ffi = cffi.FFI()
ffi.cdef("""
    typedef size_t lzma_vli;
    typedef lzma_vli lzma_vli;

    typedef struct {
        ...;
    } lzma_stream;
    typedef lzma_stream lzma_stream;

    typedef struct {
        ...;
    } lzma_allocator;
    typedef lzma_stream lzma_stream;

    typedef enum {
        LZMA_OK=0,
        /* [...] */
    } lzma_ret;

    typedef enum {
        /* [...] */
        LZMA_FORMAT_ALONE,
        LZMA_FORMAT_XZ,
        LZMA_FORMAT_RAW,
    } lzma_format;

    typedef enum {
        /* [...] */
        LZMA_FILTER_LZMA
