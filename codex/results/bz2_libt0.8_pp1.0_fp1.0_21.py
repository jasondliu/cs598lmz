import bz2
bz2f = bz2.open(sys.argv[2], 'wt')

import gzip
gzf = gzip.open(sys.argv[3], 'wt')

with open(sys.argv[1], 'rt') as f:
    for line in f:
        lf.write(line)
        bz2f.write(line)
        gzf.write(line)

lf.close()
bz2f.close()
gzf.close()
</code>
You could also consider using a memory mapping (the <code>mmap</code> module) to read the compressed results back but I'm not sure that is 100% necessary.

