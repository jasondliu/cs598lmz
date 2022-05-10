import bz2
bz2.decompress(data)

# The returned string is 'This is the original text.'

# Example 2

import bz2
uncompressable = b'hello world!hello world!hello world!hello world!'
data = bz2.compress(uncompressable)
len(data)

# 11

# 39
# Example 3

import bz2
uncompressable = b'a'*10
data = bz2.compress(uncompressable)
len(data)

# 31

# 40
# Example 4

import bz2
uncompressable = b'a'*100
data = bz2.compress(uncompressable)
len(data)

# 41

# 41
# Example 5

import bz2
uncompressable = b'a'*1000
data = bz2.compress(uncompressable)
len(data)

# 42

# 42
# Example 6

import bz2
uncompressable = b'a'*10000
data =
