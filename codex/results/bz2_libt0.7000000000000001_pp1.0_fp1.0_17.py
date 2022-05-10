import bz2
bz2.decompress(bz2_file.read())

# TODO: Use bz2.BZ2File to open the file instead of decompressing it into memory first
# with open(path_to_bz2_file) as bz2_file:
#     pass

# TODO: Check that the data is the same as original
# ...


# TODO: Test the many other functions of the bz2 module


# TODO: Verify that the compression is indeed better than standard zip compression
# ...


# TODO: Test gzip and lzma compression using their respective modules


# TODO: Test zip file compression using the zipfile module
# TODO: Test the getinfo and extract functions of the ZipFile class
# TODO: Test adding files to the archive using writestr and write
# TODO: Test extracting files from the archive using extract and extractall
