from lzma import LZMADecompressor
LZMADecompressor().decompress(open("/home/ubuntu/workspace/samples/sample1.lzma", "rb").read())

# Using LZMAUtil
import lzma
lzma.decompress(open("/home/ubuntu/workspace/samples/sample1.lzma", "rb").read())

# Using lzmaffi
from lzmaffi import LZMAFile
LZMAFile(open("/home/ubuntu/workspace/samples/sample1.lzma", "rb")).read()

# Using pylzma
import pylzma
pylzma.decompress(open("/home/ubuntu/workspace/samples/sample1.lzma", "rb").read())

# Using backports.lzma
import backports.lzma
backports.lzma.decompress(open("/home/ubuntu/workspace/samples/sample1.lzma", "rb").read())

# Using pyliblzma
import pyliblzma
pyliblz
