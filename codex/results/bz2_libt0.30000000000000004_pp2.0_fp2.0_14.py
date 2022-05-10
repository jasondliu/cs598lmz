import bz2
bz2.decompress(data)

# bz2.decompress(data)
# 'hello world!hello world!hello world!hello world!'

# bz2.compress(data)
# 'BZh91AY&SY\x94\x8c\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# bz2.compress(data)
# 'BZh91AY&SY\x94\x8c\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# bz2.decompress(bz2.compress(data))
# 'hello world!hello world!hello world!hello world!'

# bz2.decompress(bz2.compress(data))
# '
