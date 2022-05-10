from _struct import Struct
s = Struct.__new__(Struct)
fmt = '<3s3sHH'
buf = bytes(26)
s.clear()
s.set_format(fmt, buf)
name, date, time, checksum = 'FAT16', (1980, 1, 1), (0, 0, 0), 0
s.pack_into(date, time, checksum)
print(buf)
