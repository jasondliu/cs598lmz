import lzma
lzma.LZMAError

from . import _lzma

# This is a copy of the lzma module's LZMAFile class, with the
# following modifications:
#
# - The constructor takes an additional "mode" argument which is
#   passed to the underlying file object.
#
# - The file object is closed when the LZMAFile is closed.
#
# - The file object is not closed when the LZMAFile is garbage
#   collected.
#
# - The file object is not closed when the LZMAFile is finalized.
#
# - The file object is not closed when the LZMAFile is finalized.
#
# - The file object is not closed when the LZMAFile is finalized.
#
# - The file object is not closed when the LZMAFile is finalized.
#
# - The file object is not closed when the LZMAFile is finalized.
#
# - The file object is not closed when the LZMAFile is finalized.
#
# - The file object is not closed when the LZMAFile is finalized.
#
#
