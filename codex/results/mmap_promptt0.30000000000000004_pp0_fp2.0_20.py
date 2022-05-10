import mmap
# Test mmap.mmap(0, 1, "shared", mmap.MAP_SHARED, 0, 0)

# /usr/include/x86_64-linux-gnu/bits/mman.h:
# #define MAP_SHARED  0x01  /* Share changes.  */
# #define MAP_PRIVATE 0x02  /* Changes are private.  */
# #define MAP_TYPE    0x0f  /* Mask for type of mapping.  */
# #define MAP_FIXED   0x10  /* Interpret addr exactly.  */
# #define MAP_FILE    0
# #define MAP_ANONYMOUS 0x20  /* Don't use a file.  */
# #define MAP_ANON    MAP_ANONYMOUS
# #define MAP_32BIT   0x40  /* Only give out 32-bit addresses.  */
# #define MAP_GROWSDOWN  0x0100  /* Stack-like segment.  */
# #define MAP_DENYWRITE  0x0800  /* ETXTBSY */
# #define MAP_EXECUTABLE 0x
