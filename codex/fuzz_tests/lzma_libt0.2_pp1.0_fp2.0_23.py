import lzma
lzma.LZMAError: Error -3 while decompressing data: invalid distances set
</code>
I am using Python 3.6.5 on Windows 10.
I have tried to install lzma using pip and conda, but it doesn't work.
I have also tried to install pylzma, but it doesn't work either.
How can I fix this?


A:

I had the same problem.
I solved it by installing the wheel file from here:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pylzma

