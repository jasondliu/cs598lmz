from lzma import LZMADecompressor
LZMADecompressor()
</code>
I'm using Python 3.6.2, and I installed the backports.lzma module from the download page (https://pypi.python.org/pypi/backports.lzma#downloads).  I've also tried downloading and installing the tar.gz version.
The downloaded module contains a file named "lzma.py".  I can import "lzma", but that doesn't yield anything useful.
https://docs.python.org/3/library/lzma.html
https://docs.python.org/2/library/lzma.html


A:

OK, I got it.  I don't know why this worked, but I downloaded backports.lzma-0.0.8.tar.gz.  I then created a Python virtual environment, and installed the tar.gz file into the virtual environment.  Yes, I had to untar it and cd into the subdirectory, but Python seemed to be able to find the stuff.

