import mmap
# Test mmap.mmap
#
# This is a simple test to check the mmap module.
#
# This test assumes that:
#  - mmap.PAGESIZE is 4096
#  - mmap.ALLOCATIONGRANULARITY is 65536
#  - The system has at least 128 MB of free memory
#  - The system has at least one free file descriptor
#
# It is recommended to run this test on a freshly booted system,
# to avoid interference from other running programs.

# We use the system file /dev/zero to allocate memory
# Use /dev/shm/ if it exists, as it is a memory-based file system
# (e.g. tmpfs on Linux)
if os.path.exists('/dev/shm'):
    devZero = '/dev/shm/devZero'
    f = open(devZero, 'wb')
    f.close()
else:
    devZero = '/dev/zero'

# We use a temporary file to store the data
tmpFile = tempfile.mktemp()

# We use a temporary file to store the data
tmpFile
