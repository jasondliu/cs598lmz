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
if hasattr(sys, 'frozen'):
    _boot_path = os.path.dirname(sys.executable)
else:
    _boot_path = os.path.dirname(os.path.dirname(__file__))
    # print('_boot_path is ', _boot_path)
sys.path.insert(0, _boot_path)

# On AIX, 'LD_LIBRARY_PATH' is used instead of 'PATH'.
if os.name == 'posix' and sys.platform == 'aix5
