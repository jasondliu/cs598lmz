from lzma import LZMADecompressor
LZMADecompressor(size=size)


# Call this before the LZMADecompressor ctor, 
# otherwise it segfaults
s = lzma.decompress(compressed)

# The rest works fine
d = LZMADecompressor(size=size)
out = d.decompress(compressed)
</code>
Is it a bug in lzma, or am I doing something wrong? Any help is appreciated! 


A:

I can now confirm that this is certainly a bug in the <code>lzma</code> module.
Thanks to the hint that this may be a problem relative to <code>fork</code>, I added a <code>fork</code> call in my code to test the theory. This allowed me to consistently reproduce a segmentation fault, irregardless of whether I used <code>size</code> or not. 
This makes the workaround above unfeasible. We filed a bug report on the public Python repository, and the Python team is already working on fixing this.

