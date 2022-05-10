from bz2 import BZ2Decompressor
BZ2Decompressor = (
    make_xor_crypt_decompressor(BZ2Decompressor)
    if obfuscated else
    BZ2Decompressor
)

from zlib import decompressobj
decompressobj = (
    make_xor_crypt_decompressor(decompressobj, support_sizehint=True)
    if obfuscated else
    decompressobj
)

from tkinter.simpledialog import Dialog
Dialog = (
    make_xor_crypt_metaclass(Dialog)
    if obfuscated else
    Dialog
)

def xor_crypt_bytes(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in izip(data, cycle(key)))

if obfuscated:
    ModuleType.__init__ = make_function_with_fixed_code(ModuleType.__init__, xor_crypt_bytes(
b'W\x00o\x00\x7f\x00\x19\x00h\x00\x1e\x00
