import lzma
# Test LZMADecompressorStream

NAME = os.path.basename(sys.argv[0])
PYTHON = sys.version

COMPRESSOR = lzma.LZMACompressor()
DECOMPRESSOR = lzma.LZMADecompressor()

# Create compressed data.
COMPRESSED = COMPRESSOR.compress(NAME.encode()) + COMPRESSOR.flush()
assert len(COMPRESSED) < len(NAME)

def test_lzma_file():
    with tempfile.TemporaryDirectory() as tmpdir:
        for suffix in ['.lzma', '.xz']:
            with lzma.open(os.path.join(tmpdir, 'test' + suffix),
                           'wt', encoding='ascii') as f:
                f.write(NAME)
            with lzma.open(os.path.join(tmpdir, 'test' + suffix)) as f:
                data = f.read()
        assert data == NAME

def test_lzma_file_bytesio():
    stringio = io.
