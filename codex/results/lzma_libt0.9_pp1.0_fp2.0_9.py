import lzma
lzma.LZMACompressor

except:

return False

return True

def split_list(list, n):

"""

>>> split_list([0, 1, 2, 3, 4, 5, 6], 3)

[[0, 1, 2], [3, 4, 5], [6]]

"""

m = len(list)

n = max(1, min(n, m))

s = float(m) / n

return [list[int(round(i * s)): int(round((i + 1) * s))]

for i in range(n)]

# The following gives a context-manager object that can be used with the "with"

# keyword to build specialized temporary files in a foolproof way. Data written

# to the file is flushed all the way to disk, and the file is automatically

# removed on exit from the "with" block. Unlike mkstemp(), this doesn't follow

# a symlink, and ensures that the directory we create in has the same permission

# flags as the ultimate temporary file.

