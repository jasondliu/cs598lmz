from lzma import LZMADecompressor
LZMADecompressor()

# Here's another way to use a context manager

with open('shout.txt', 'rt') as f:
    text = f.read()
    print(text)

# open() can also be used with a context manager as well,
# and that's what we'll do in the next part of this course.

# But here's how to do it with a `with` statement:

import lzma
with lzma.open('shout.xz') as f:
    text = f.read()
    print(text)


# Let's look at another example.
# Here's a file-like object called `StringIO`:

from io import StringIO
f = StringIO()
f.write('Hello\n')
f.write('World\n')

print('This is a test', file=f)

f.seek(0)
text = f.read()
print(text)

# What we did here was write a couple of things
# to a file-like object, and then later we read it.
# It's just like reading a
