import mmap
# Test mmap.mmap(fileno, length, access=ACCESS_DEFAULT, offset=0, tagname=None)
# create a new memory map
#
#     fileno
#         An integer file descriptor of the file to be memory mapped, i.e., the
#         result of a file object’s fileno() method.
#
#     length
#         The size of the memory map in bytes. This must be less than or equal
#         to the size of the underlying file.
#
#     access
#         The type of access. Possible values are ACCESS_READ, ACCESS_WRITE,
#         ACCESS_COPY, or ACCESS_DEFAULT. The default is ACCESS_DEFAULT, which
#         ensures that modifications to the content of the memory map do not
#         affect the original file, and that modifications to the original file
#         do not affect the content of the memory map.
#
#     offset
#         The starting offset of the file to map.
#
#     tagname
#         The tagname argument is only used on Windows. It specifies the tag
#         name of a
