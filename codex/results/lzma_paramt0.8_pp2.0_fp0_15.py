from lzma import LZMADecompressor
LZMADecompressor().decompress(open("test_small.xz", "rb").read())
</code>
Or
<code>subprocess.run("xz -d test_small.xz")
</code>
Or
<code>subprocess.run("xz -d test_small.xz -c &gt; test_small.txt")
</code>
My problem is that I need to do it hundreds of thousands of times.  So, I'd like to find a parallel compression library.


A:

I ended up using the multiprocessing library.  Here's the code:
<code>import subprocess
from multiprocessing import Pool
import os

def xz_decompress(fname):
    subprocess.run(["xz", "-d", fname])

if __name__ == '__main__':
    files = os.listdir("./")
    compressed = [f for f in files if f.endswith(".xz")]
    pool = Pool(processes=6)
    pool.map(xz_decompress, compressed
