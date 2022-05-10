import mmap
# Test mmap.mmap

# This is a test for mmap.mmap.
# It was written to show the problem with mmap.mmap when used to replace
# a file.  It turns out that the problem is not with mmap, but with the
# way I was using it.

# This program does the following:
# 1. Create a file with a single line of text.
# 2. Map the file into memory.
# 3. Replace the text in the file with a different line of text.
# 4. Unmap the file.
# 5. Map the file into memory again.
# 6. The new text should be visible.

# The problem I was having was that the new text was not visible.
# It turns out that the problem was that I was not unmapping the file
# before overwriting it.  Once I added that, the new text was visible.

import mmap

# Create a file with a single line of text.
f = open('test.txt', 'w+')
f.write('This is a test\n')
f.close()

# Map the file into memory.

