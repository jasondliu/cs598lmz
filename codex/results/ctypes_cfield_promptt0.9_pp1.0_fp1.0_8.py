import ctypes
# Test ctypes.CField's ability to define a field in a structure by adding/replacing
# a field
import ctypes.test.test_cfield

so_prefix = ""
csuffix = ""
suffix = ""
prefix = ""
src_suffix = ".c"
output_src_dir = ""
prefix_cflags = ["-fPIC", "-Wall", "-D=_GNU_SOURCE"]
src_dir = os.path.join('..', 'test', 'src')

# get the shared object name
for cflag in sys.argv:
    if cflag[:2] == "-o":
        so_prefix = cflag[2:]

# distinguish different builds on the same host
if hasattr(sys, "gettotalrefcount"):
    csuffix = "_pydebug"

# make a string with the same length as current time to avoid name
# collision
suffix = "_" + str(time.time()).replace(".", "")

# set the prefix
prefix = so_prefix + csuffix + suffix

lib = ctypes.util.find_
