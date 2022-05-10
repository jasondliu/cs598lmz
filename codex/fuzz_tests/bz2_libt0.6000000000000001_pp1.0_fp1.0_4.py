import bz2
bz2_comp = bz2.BZ2Compressor()
with bz2.open("mylog.bz2", "wt") as f:
    for line in lines:
        f.write(bz2_comp.compress(line))
        f.write("\n")
    f.write(bz2_comp.flush())
!ls -l mylog.*

!cat mylog.bz2 | bzcat

# Example: Compressing Data in Memory
import bz2
original_data = b"This is the original text."
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# Example: Decompressing Streams
import bz2
original_data = b"This is the original text."
print('Original     :', len(original_data), original_data
