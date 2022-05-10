import _struct
# Test _struct.Struct

# 1. Create a struct object
# 2. Create a buffer object
# 3. Unpack the buffer object using the struct object

# 1. Create a struct object
# struct.Struct(format)
# format: c = char, b = signed char, B = unsigned char
#         h = short, H = unsigned short
#         i = int, I = unsigned int
#         l = long, L = unsigned long
#         q = long long, Q = unsigned long long
#         f = float, d = double
#         s = char[]
#         p = char[], P = void *

# Create a struct object
# Format: 2 unsigned short, unsigned int, 2 unsigned short, unsigned int
#         2 unsigned short, unsigned int, 2 unsigned short, unsigned int
#         2 unsigned short, unsigned int, 2 unsigned short, unsigned int
#         2 unsigned short, unsigned int, 2 unsigned short, unsigned int
#         2 unsigned short, unsigned int, 2 unsigned short, unsigned int
#         2 unsigned short, unsigned int, 2 unsigned short, unsigned int
#         2 unsigned short, unsigned int, 2 unsigned short
