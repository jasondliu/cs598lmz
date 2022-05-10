import lzma
lzma.__doc__ = """
LZMA compression and decompression

This module provides a simple interface to compress and decompress files just
like the GNU programs xz and unxz would.

It supports the LZMA, XZ and legacy LZMA file formats.

The data format used by XZ Utils is a simple container format called the .xz
format. It can contain one or more compressed files. The .xz format is
container format and not a compression format.

The .xz format is designed to be as simple as possible and has been
optimized for high compression ratio. It is possible to compress or
decompress a single file represented by a regular file, a block device,
or a stream of data, but not a directory.

The .xz format does not specify how the data is compressed. The
compression method is specified separately. Currently the only
compression method supported by this module is LZMA2, which is used by
XZ Utils, PeaZip, FreeArc, and 7-Zip since version 9.20.

The LZMA2 compression method used by the xz command
