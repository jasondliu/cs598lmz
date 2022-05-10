import bz2
bz2c = bz2.BZ2Compressor()
bz2c.compress(data)
bz2c.flush()
bz2c

</code>
I'm quite certain that the underlying code has not changed, but the behavior may have in terms of a bug fix or change in the default parameters.
<code>&gt; python3 --version
Python 3.7.4
&gt; python3 -c "import sys; print(sys.version)"
3.7.4 (default, Sep  7 2019, 18:35:08) 
[GCC 9.2.1 20190827 (Red Hat 9.2.1-1)]

</code>

