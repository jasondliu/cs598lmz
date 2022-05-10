import io
# Test io.RawIOBase
#   .read(size=-1)
#
# Test io.BufferedIOBase
#   .read(size=-1)
#   .read1(size=-1)
#   .readinto(b)
#   .readinto1(b)
#   .readinto(buffer)
#
# Test io.RawIOBase
#   .write(b)
#
# Test io.BufferedIOBase
#   .write(b)
#   .flush()
#   .seek(offset, whence)
#   .tell()
#   .truncate(size)
#   .fileno()
#
# Test io.IOBase
#   .close()
#   .isatty()
#   .next()
#   .readable()
#   .seekable()
#   .writable()

# TODO(pts): Add tests for io.RawIOBase.readinto1()

# TODO(pts): Add tests for io.BufferedIOBase.getvalue()
# TODO(pts): Add tests for io.BufferedIO
