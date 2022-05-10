from lzma import LZMADecompressor
LZMADecompressor

decompressor = LZMADecompressor()

while True:
    # Get the size of the file and the compressed block from the
    # uncompressed stream
    file_size, = f.unpack('Q')
    block_size, = f.unpack('Q')
    if not block_size:
        break
    block = decompressor.decompress(f.read(block_size))
    print(f"{file_size}, {block_size}")
    print(block)
    output_filename = os.path.basename(input_path) + '.{}.sas7bdat'.format(index)
    with open(output_filename, 'wb') as g:
        g.write(block)
    index += 1
</code>
<blockquote>
<p>when I uncompress, I obtain the following:
  <code>&lt;code&gt;FONCTION ssdecompressValue(pValue)
   DIM pValue_size as long
   DIM pValue_compressed as long, byVal
   DIM
