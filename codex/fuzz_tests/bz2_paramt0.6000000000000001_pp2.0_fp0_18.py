from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
I am running Python 2.7.3 on a 64-bit Ubuntu 12.04.
Does anyone know what to do?


A:

First, I would try to install a newer version of python. 
Second, it seems that the bz2 module is compiled for 32 bit machines. The following link describes how to compile the module for your 64 bit machine.

