import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

def decompress(compr):
    with lzma.open(compr,'rb') as fh:
        return fh.read()

# Usage:
print(decompress('data/fastq/SRR079881_1.fastq.lzma'))

# Output:
# b'@SRR079881.69 HWI-ST915_0247:7:1:14:915 length=70\nCGTAGTTCAGTGAGCTATGCATGAAGCATGCGTTTGAGCCTGTATTGTACGGTCTTAAGAGATTGCCGACT\n+SRR079881.69 HWI-ST915_0247:7:1:14:915 length=70\nIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII\n@SRR079881.
