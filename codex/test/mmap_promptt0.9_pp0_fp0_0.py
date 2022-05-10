import mmap
# Test mmap.mmap implementation

# Note py27/py34 have different mmap implementations
PY3 = sys.version > '3'

# Only test read-write shared mapping on systems that are known to work
if sys.platform not in ('win32', 'openbsd5'):
    from os import chmod
    from stat import S_IRUSR, S_IWUSR, S_IRGRP, S_IWGRP, S_IROTH, S_IWOTH
    open("data1", "w").write("ABC")
    chmod("data1", S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH)

    # Jython has a BufferUnderflowException if the source string is empty
    if sys.platform != 'java':
        open("data2", "w").write("DEF")
        chmod("data2", S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH | S_IWOTH)
