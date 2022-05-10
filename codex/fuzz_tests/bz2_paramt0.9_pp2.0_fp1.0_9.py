from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(read_file("res/raw.bz2"))

# xxd
from binwalk.modules.signature import Signature
Signature("-q -E").run("res/raw.bz2")
exit(1)

# dumps
from binwalk.common import BlockFile
for block in BlockFile("res/raw.bz2"):
  print("%s %s %s %s %s %s" % (block.shannon_entropy(), block.offset(), block.size(), block.size(), block.size(), block.size()))

# extract
with Extractor(blocksize=0x2000000, search=False) as extractor:
  extractor.scan("res/raw.bz2", extract=False, quiet=True)
extractFile("res/raw.bz2", "res/out/extract")

# hexdump
print("Hexdump:")
with Hexdump("-C -n 0") as hexdump:
  hexdump.run("res/out/extract/0")

# carve
# carve("res
