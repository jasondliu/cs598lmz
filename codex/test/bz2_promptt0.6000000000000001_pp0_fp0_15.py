import bz2
# Test BZ2Decompressor, BZ2Compressor classes

def test_bz2_decompressor():
    # Test the BZ2Decompressor class.
    #
    #     - check the decompress() method
    #     - check the flush() method
    #     - check the unused_data attribute
    #     - check the eof attribute
    #     - check the unconsumed_tail attribute
    #     - check the max_length argument
    #     - check the decompressor is stateful
    #     - check the decompressor can be used as a context manager
    #     - check the decompressor's state is not modified by the context manager
    #     - check the decompressor can decompress multiple streams in sequence
    #     - check multiple decompressors can decompress a single stream in sequence
    #     - check multiple decompressors can decompress a single stream in parallel
    #     - check multiple decompressors can decompress multiple streams in parallel

    # Check the decompress() method
    d = bz2.BZ2Decompressor()
    assert d.decompress(b"BZh9")
