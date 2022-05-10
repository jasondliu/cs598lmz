from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Solve the second part of this puzzle:

# 1. Let's create a new compression format called pickle.bz2. This format will
#    apply bz2 compression to the pickle of an object.
# 2. Create an equivalent my_unpickle_bz2(data) function that takes in your
#    compressed data, unpickles it, then decompresses it.
# 3. Apply my_unpickle_bz2() to the result of the function in step 1.
# 4. Create an equivalent my_pickle_bz2(data) function that compresses the
#    pickle of any object.
# 5. Create a function that takes in the compressed data as a parameter,
#    decompresses
