import lzma
lzma.decompress("a"*100000)
</code>
In both cases, the RAM usage is much higher than the size of the input data. I'm running Python 3.6.4 on a 64-bit Windows 10 system.
Is this expected behavior? Is there any way to control how much memory is used?

