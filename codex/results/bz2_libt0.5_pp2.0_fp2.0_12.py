import bz2
bz2.decompress(compressed)

# <codecell>

from bz2 import decompress
decompress(compressed)

# <codecell>

from bz2 import BZ2Decompressor
d = BZ2Decompressor()
d.decompress(compressed)

# <codecell>

d.decompress(compressed)

# <codecell>

d.unused_data

# <codecell>

d.decompress(d.unused_data)

# <codecell>

d.unused_data

# <codecell>

d.decompress(d.unused_data)

# <codecell>

d.unused_data

# <codecell>

d.decompress(d.unused_data)

# <codecell>

d.unused_data

# <codecell>

d.decompress(d.unused_data)

# <codecell>

d.unused_data


