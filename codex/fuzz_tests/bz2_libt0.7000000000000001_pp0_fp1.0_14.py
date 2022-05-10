import bz2
bz2.decompress(bz2_data)

# output: b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# Magic number: BZh
# h: 2^20 blocksize
# 9: 9% block compression ratio
# 1A: .001
# &: begin block, end of block info
# S: randomised
# Y: max number of elements in Huffman code
# A: alphabet size of Huffman code
# \xaf: Huffman code
# \x82: Huffman code
# \r: special end-of-stream marker
# \x00\x00\x01\x01\x80: 32 bits of randomised data
# \x02: 2^6 (64) literal Huffman tables
# \xc0: Huffman code
# \x02: 2
