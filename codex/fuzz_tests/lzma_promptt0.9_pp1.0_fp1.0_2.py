import lzma
# Test LZMADecompressor to decompress a file in memory,
# without creating a temporary file

with open('/path/to/my/file.xz', 'rb') as in_file:
    decomp = lzma.LZMADecompressor()
    try:
        #input_size = os.path.getsize('/path/to/my/file.xz')
        input_size = 420 # Total: 2770.0 KiB
        print("Total: {0:,.1f} MiB".format((sys.getsizeof(in_file.read())/1024)/1024))
    finally:
        in_file.close()
    with open('/path/to/myfile', 'wb') as outfile:
        while True:
            # open file, decompress using lzma, write to disk
            chunk = in_file.read(input_size)
            if not chunk:
                break
            result = decomp.decompress(chunk)
            outfile.write(result)
</code>
I've read through numerous posts, but my lack of knowledge makes it really difficult
