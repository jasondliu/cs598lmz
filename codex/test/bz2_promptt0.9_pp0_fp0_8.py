import bz2
# Test BZ2Decompressor with decompress() called before first read
#
# bzr version-info
# revno: 4997
# branch nick: 2.6.0b2
# repository branch: trunk
# timestamp: 2009-12-07 17:40:40 +0000
# build-date: 2009-12-07 16:54:46 +0000
# python version: 2.6.4
# Platform: Windows-Vista-6.0.6001-SP1
# compiler: MSC v.1500
test_string = 'This is the input string for decompress()'
test = bz2.BZ2Compressor(2)
