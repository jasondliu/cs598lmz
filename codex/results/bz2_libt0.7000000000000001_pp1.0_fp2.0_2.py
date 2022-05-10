import bz2
bz2.decompress(data)

# 比较一下压缩前后的大小
import bz2
original_data = b'This is the original text.'
print('Original:{},{} bytes'.format(original_data, len(original_data)))
compressed = bz2.compress(original_data)
print('Compressed:{},{} bytes'.format(compressed, len(compressed)))
decompressed = bz2.decompress(compressed)
print('Decompressed:{},{} bytes'.format(decompressed, len(decompressed)))

# bz2.compress 与 bz2.decompress 使用的是 BZ2 算法。
# 这个算法是在内存中进行压缩和解压缩的，因此，
# 压缩的结果必须先
