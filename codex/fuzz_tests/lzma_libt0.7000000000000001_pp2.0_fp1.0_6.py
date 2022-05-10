import lzma
lzma.open(infile, "rt")
</code>
I want to do something like this:
<code>import gzip

with gzip.open(infile, "rt") as f:
    # write file to outfile
    # if outfile.extension in ['.xz', '.lzma']
</code>


A:

You can wrap it in another file, and open that instead:
<code>import lzma

with open(infile, 'rb') as f:
    with lzma.open(f, "rt") as xzf:
        xzf.read()
</code>

