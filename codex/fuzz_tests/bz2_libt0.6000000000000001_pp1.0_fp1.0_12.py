import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# 'Hello World!'

# 哈夫曼算法
from huffman import HuffmanCoding

h = HuffmanCoding('hello world!')
print(' The string is : ' + h.stringData)
print(' The dictionary is : ' + str(h.char_freq))
print(' The total length is : ' + str(h.total_length))

output_data = h.compress()
print(' The compressed data is : ' + str(output_data))
print(' The compressed length is : ' + str(len(output_data)))
print(' The compression ratio is : ' + str(h.compression_ratio()))

decompressed_data = h.decompress(output_data)
print(' The original string is : ' + decompressed_data)

# 再次强调，哈夫曼算法是一种无损数
