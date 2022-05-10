from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(pickle.dumps(False))

#<module '_pickle' from '/usr/lib/python3.6/lib-dynload/_pickle.cpython-36m-x86_64-linux-gnu.so'>
#<function BZ2Decompressor.decompress at 0x7f62e03959d8>
#b'\x80\x03\x00\x00\x00\x00'
