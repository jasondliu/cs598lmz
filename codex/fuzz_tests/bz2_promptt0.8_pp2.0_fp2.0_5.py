import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    with open("/Users/kenjisato/Downloads/sample.txt.bz2", "rb") as f:
        file_content = f.read()
        un_content = decompressor.decompress(file_content)
        print(un_content)

# Test BZ2File
with bz2.BZ2File("/Users/kenjisato/Downloads/sample.txt.bz2") as f:
    file_content = f.read()
    print(file_content)
    

# Test BZ2File write
import bz2
value = b"Hello world"
with bz2.BZ2File("/Users/kenjisato/Downloads/hello_world.txt.bz2", "wb") as f:
    f.write(value)
    
    
# Test BZ2Compressor
s = b"This is the example"

compressor = bz2.BZ2Compressor()
compressed_data = compressor.
