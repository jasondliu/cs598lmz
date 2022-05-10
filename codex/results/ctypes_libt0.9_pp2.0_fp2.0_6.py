import ctypes
ctypes.cdll.LoadLibrary('libX11.so')
</code>
It's not so fast as the native Linux X11 library but I've tested it on multiple machines, including a Raspberry PI and it works.

