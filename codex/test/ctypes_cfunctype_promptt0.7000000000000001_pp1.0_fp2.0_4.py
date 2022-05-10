import ctypes
# Test ctypes.CFUNCTYPE()
#
# Windows x86_64
#   VS2015, VS2017: 32bit, 64bit
#   clang-cl 6.0, 8.0: 32bit, 64bit (with -m32, -m64)
#   mingw-w64 8.1.0: 32bit, 64bit (with -m32, -m64)

# Windows x86
#   VS2015, VS2017: 32bit
#   clang-cl 6.0, 8.0: 32bit (with -m32)
#   mingw-w64 8.1.0: 32bit (with -m32)

# Linux x86_64
#   gcc 5.4, 7.3: 64bit (with -m64)
#   clang 6.0, 8.0: 64bit (with -m64)

# Linux x86
#   gcc 5.4, 7.3: 32bit (with -m32)
#   clang 6.0, 8.0: 32bit (with -m32)

# MacOS X86_64
#   Xcode
