import bz2
bz2.decompress(bz2_compressed_data)

# split
# split(s, n)
# Split a string into a list of strings of length n.
# If the last string is shorter than n, the last string will be padded with spaces.
# Example:
# >>> split("Hello world", 2)
# ['He', 'll', 'o ', 'wo', 'rl', 'd ']

# join
# join(s, lst)
# Join a list of strings lst into a single string s, using s as the separator.
# Example:
# >>> join(" ", ['Hello', 'world'])
# 'Hello world'

# find
# find(s, sub)
# Return the lowest index in s where the substring sub is found,
# such that sub is contained within s[start:end]. Return -1 on failure.
# Example:
# >>> find("Hello world", "or")
# 7
# >>> find("Hello world", "chicken")
# -1

# rfind
# rfind(s, sub)
# Return the highest index
