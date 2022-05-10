import lzma
lzma.LZMADecompressor()

# Test that we can import "lzma" without "lzma.LZMADecompressor"
import lzma

# Test that we can import "lzma.LZMADecompressor" without "lzma"
from lzma import LZMADecompressor

# Test that we can import "lzma.LZMADecompressor" with "lzma"
import lzma
from lzma import LZMADecompressor

# Test that we can import "lzma.LZMADecompressor" with "lzma" and "lzma.LZMADecompressor"
import lzma
from lzma import LZMADecompressor
from lzma import LZMADecompressor

# Test that we can import "lzma.LZMADecompressor" with "lzma" and "lzma.LZMADecompressor" and "lzma"
import lzma
from lz
