import mmap
# Test mmap.mmap(-1, length, prot=mmap.PROT_READ|mmap.PROT_WRITE, flags=mmap.MAP_SHARED, fd=None, offset=0)
# https://stackoverflow.com/questions/38476700/how-to-use-mmap-in-python-3-5
# https://stackoverflow.com/questions/54671573/why-does-mmap-map-write-fail-on-windows


# https://github.com/siddontang/ledisdb/blob/master/ledisdb/db/mmap_file.go
# https://github.com/siddontang/ledisdb/blob/master/ledisdb/config/config.go
# https://github.com/siddontang/ledisdb/blob/master/ledisdb/db/db.go
# https://github.com/siddontang/ledisdb/blob/master/ledisdb/db/fragment.go
# https://github.com/siddontang/
