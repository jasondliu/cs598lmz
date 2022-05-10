import lzma
lzma.decompress(b'\x00'*16 + data)

# data = b'\x00'*16 + data
# with open('test_file', 'wb') as f:
#     f.write(data)

# import lzma
# with lzma.open('test_file', mode='rb') as f:
#     f.read()

# from py7zlib import Archive7z
# with open('test_file', 'rb') as f:
#     archive = Archive7z(f)
#     print(b''.join(archive.getnames()))
#     for name in archive.getnames():
#         contents = archive.getmember(name).read()

# import ctypes
# ctypes.cdll.LoadLibrary('./liblzma.so')
# lib = ctypes.cdll.LoadLibrary('./liblzma.so')
# lib.lzma_easy_decoder(data, len(data), len(data), 5)

# import pylzma
# pylzma
