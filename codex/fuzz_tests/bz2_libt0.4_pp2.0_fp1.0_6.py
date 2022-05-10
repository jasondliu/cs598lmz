import bz2
bz2.BZ2File(filename).read()

# or

import bz2
bz2.decompress(open(filename).read())
</code>

