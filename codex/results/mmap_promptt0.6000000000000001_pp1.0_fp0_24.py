import mmap
# Test mmap.mmap to make sure it works.
#
# A 10-byte buffer should be created.
#
# >>> mm.read(1)
# '\x00'
# >>> mm.read(9)
# '0123456789'
# >>> mm.read(1)
# ''
# >>> mm.write('abcdefghij')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: cannot write 1 bytes at offset 0: mmap.ALLOCATIONGRANULARITY=4096
# >>> mm.write('abcdefghijklmnopqrstuvwxyz')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: cannot write 26 bytes at offset 0: mmap.ALLOCATIONGRANULARITY=4096
# >>> mm.seek(0)
# 0
# >>> mm.read(1)
# '\x00'
# >>> mm.read(9)
# '0123456789'
# >>> mm
