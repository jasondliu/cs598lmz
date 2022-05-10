import lzma
# Test LZMADecompressor on some data
with gzip.open('bzipped', 'rb') as f_in, open('bunzipped', 'wb') as f_out:
    f_out.write(lzma.decompress(f_in.read()))
# Test LZMACompressor and LZMADecompressor on some data
with open('comp.bin', 'wb') as f_out:
    with lzma.open('lzmaed', 'w', preset=9) as f_comp:
        f_comp.write(b'the quick brown fox jumped over the lazy dog')
with lzma.open('lzmaed') as f_lzma:
    file_content = f_lzma.read()
    print('read: {!r}'.format(file_content))
with open('unlzmaed', 'wb') as f_out:
    f_out.write(file_content)
pprint(file_content)

# To archive data, in a tar.bz2 file
tar = tarfile.open("samples.
