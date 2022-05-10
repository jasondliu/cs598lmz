import mmap
# Test mmap.mmap()
#
# This test is based on the test_mmap.py test from the Python 2.7.3
# standard library.
#
# The mmap module defines the following class:
#
# class mmap(object):
#     '''Memory-mapped file support.'''
#
#     def __init__(self, fileno, length, tagname=None, access=mmap.ACCESS_DEFAULT, offset=0):
#         '''Initialize the mmap object.
#
#         The arguments are:
#         fileno -- this is the file descriptor of the file to map.
#         length -- the number of bytes to map (cannot be changed later).
#         tagname -- name of the shared memory object.
#         access -- one of ACCESS_READ, ACCESS_WRITE, or ACCESS_COPY.
#         offset -- the offset in the file where the mapping starts.
#         '''
#
#     def close(self):
#         '''Close the mmap object, so it no longer affects the underlying
#         file.
#        
