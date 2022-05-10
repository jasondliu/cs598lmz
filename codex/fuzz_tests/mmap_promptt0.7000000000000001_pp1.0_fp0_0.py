import mmap
# Test mmap.mmap():
# - create new file
# - create mapping
# - write data to file
# - close file
# - reopen file
# - map to file
# - compare data to original
# - close file
# - reopen file
# - move cursor
# - read in data at different offset
# - unmap file
# - close file
# - reopen file
# - map to file
# - compare data
# - unmap file
# - close file
# - reopen file
# - map to file
# - compare data to original
# - close file
# - reopen file
# - move cursor
# - read in data at different offset
# - unmap file
# - close file
# - reopen file
# - map to file
# - compare data
# - unmap file
#
#
# Steps for all test cases:
# 1. Open file for read/write
# 2. Create mmap object
# 3. Create data to write into file
# 4. Write data to mmap object
# 5. Get file size
# 6. Close file
# 7. Reopen file
# 8. Create mm
