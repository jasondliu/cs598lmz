import bz2
# Test BZ2Decompressor.flush() method
buf = bz2.BZ2Decompressor()
buf.flush()
buf.flush()
# Test BZ2Decompressor.unused_data property
buf = bz2.BZ2Decompressor()
buf.unused_data
buf.unused_data = b'foo'
buf.unused_data
buf.unused_data = b'bar'
buf.unused_data
buf.unused_data = b'\x00'*1000000
buf.unused_data
buf.unused_data = b'\x00'*1000000
buf.unused_data
buf.unused_data = b'\x00'*1000000
buf.unused_data
buf.unused_data = b'\x00'*1000000
buf.unused_data
buf.unused_data = b'\x00'*1000000
buf.unused_data
buf.unused_data = b'\x00'*1000000
buf.unused_data
buf.unused_data = b'
