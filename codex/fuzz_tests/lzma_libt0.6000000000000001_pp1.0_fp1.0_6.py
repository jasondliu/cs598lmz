import lzma
lzma.LZMACompressor(filters=[{"id": lzma.FILTER_LZMA1, "dict_size": 8 * 1024 * 1024, "lc": 3, "lp": 0, "pb": 2}])
</code>
While the above code works for the purposes of a library, I am more interested in the command line equivalent.
In the command line, I know that LZMA1 is the default algorithm for the lzma executable. If I try to specify the filter options, I get an error:
<code>$ lzma -9 --dict-size=8388608 --lc=3 --lp=0 --pb=2
lzma: --dict-size: Invalid value
</code>
(I also tried <code>--dict-size=8M</code>, but that throws the same error.)
I can't find any information in the man page about how to specify these options. Is there a way to do this?

