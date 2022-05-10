import bz2
bz2_data = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
print(bz2.decompress(bz2_data))

# Now repeat the exercise, but instead of decompressing, compress the data
# using bz2.compress(). You'll have to create the compressed value using
# decompressed_data and then write the value to a file to submit.
import bz2
bz2_data = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
#bz2_data = bz
