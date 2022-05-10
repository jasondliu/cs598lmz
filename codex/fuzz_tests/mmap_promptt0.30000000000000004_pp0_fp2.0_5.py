import mmap
# Test mmap.mmap()
#
# This test is not exhaustive.  It only tests the most basic functionality.
#
# The test is designed to be run in a subprocess so that it can use large
# amounts of memory without affecting other tests.
#
# XXX To do:
# - test access=ACCESS_READ, ACCESS_COPY
# - test resizing
# - test offset
# - test writing
# - test flush()
# - test move()
# - test close()
# - test seek()
# - test tell()
# - test read_byte(), read_line()
# - test writing
# - test writing past the end of the file
# - test writing before the beginning of the file
# - test resizing the underlying file
# - test that writing doesn't change the file size
# - test that writing past the end of the file does change the file size
# - test that writing before the beginning of the file does change the file size
# - test that resizing the underlying file changes the size of the mmap
# - test that resizing the underlying file doesn't change the contents of the mmap
# -
