import mmap
# Test mmap.mmap()
#
# MMAP_SHARED:  Changes are visible to other processes mapping the same region,
# and (in the case of MAP_FILE), are carried through to the underlying file.
#
# MMAP_PRIVATE: Changes are private to the process, and are never carried
# through to the underlying file.
#
# MMAP_FIXED:   The mapping must be at the requested address, and may not
# extend past the end of the file.
#
# MMAP_DENYWRITE:  Forces changes by other processes to be written to the file
# rather than to the mapping.
#
# MMAP_EXECUTABLE:  The mapping may be marked executable.

# Note:
#
# 1. Should use mmap.ACCESS_READ and mmap.ACCESS_WRITE instead of 'r' and 'w'.
# 2. mmap's filepos is in bytes, while the file's filepos is in char.
# 3. The default access of mmap is mmap.ACCESS_WRITE.
# 4. Use mmap.move(0, 0,
