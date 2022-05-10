import lzma
lzmapath = Path(lzma.__file__)
lzmamod = SourceModule("""
#include <lzma.h>

lzma_ret lzma_wrapper_compress(unsigned char *decoded, 
                               size_t decoded_size, 
                               unsigned char *encoded, 
                               size_t *encoded_size) {

    // Alloc lzma compat UTF-8 string
    uint8_t *preset_string = lzma_preset_encode_utf8(preset);
    if (!preset_string)
    {
        return LZMA_MEM_ERROR;
    }
    
    lzma_stream stream = LZMA_STREAM_INIT;
    stream.next_in = decoded;
    stream.avail_in = decoded_size;
    stream.next_out = encoded;
    stream.avail_out = *encoded_size;
    
    lzma_ret ret = lzma_easy_encoder(&stream, preset,
