import bz2
bz2.BZ2Compressor().compress(b"a")

# %load snippets/bz2.py
import bz2
assert bz2.decompress(bz2.compress(b"a")) == b"a"
 
# %load snippets/bz2.py
import bz2
assert bz2.decompress(bz2.compress(b"a")).decode() == "a"

# %load snippets/bz2.py
import bz2
assert bz2.decompress(bz2.compress(b"a")).decode() == "a"
print(bz2.decompress(bz2.compress(b"a")).decode())

# %load snippets/bz2.py
import bz2
assert bz2.decompress(bz2.compress(b"a")).decode() == "a"
print(bz2.decompress(bz2.compress(b"a")).decode())
print(bz2.
