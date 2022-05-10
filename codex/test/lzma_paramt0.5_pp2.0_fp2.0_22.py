from lzma import LZMADecompressor
LZMADecompressor()

# #############################################################################
# ################  BEGIN platform specific defines ##########################
# #############################################################################

# The following is used to augment Python's sys.path with modules
# from the PyInstaller bootloader directory.
# If some of these modules are found somewhere else on sys.path,
# e.g. in the Python standard library, this import will not replace
# them.
# This is needed for PyInstaller to bundle its own copy of select-related
# modules like "select" or "socket".
