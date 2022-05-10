from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()

if __name__ == '__main__':
    if len(sys.argv) > 2:
      for fname in sys.argv[1:]:
        with open(fname, 'rb') as f, open(fname + ".recompressed.lzma", 'wb') as fout:
            fout.write(LZMADecompressor.decompress(f.read()))
    else:
      print("Usage: python lzma-helpers.py file1 file2 file3 ....")
