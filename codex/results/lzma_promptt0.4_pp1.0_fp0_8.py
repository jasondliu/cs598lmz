import lzma
# Test LZMADecompressor
#
# The test data is a bunch of files compressed with xz.
#
# The test is to decompress the files with LZMADecompressor,
# and compare the result to the original file.

# Test data
test_data = [
    # filename, uncompressed size
    ("alice29.txt", 152089),
    ("asyoulik.txt", 125179),
    ("cp.html", 2460),
    ("fields.c", 4689),
    ("grammar.lsp", 3179),
    ("kennedy.xls", 10297),
    ("lcet10.txt", 42672),
    ("plrabn12.txt", 86089),
    ("ptt5", 40717),
    ("sum", 745),
    ("xargs.1", 10691),
]

# Test data directory
test_dir = os.path.join(os.path.dirname(__file__), 'xztestdata')

class TestLZMADecompressor(unittest.TestCase):
    def test_decompressor
