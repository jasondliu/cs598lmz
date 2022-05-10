gi = (i for i in ())
# Test gi.gi_code (which contains a "new" class object -- a generator iterator)
print(gi.gi_code.co_name)
print(gi.gi_code.co_filename)
print(gi.gi_code.co_firstlineno)

# Test tuples
t = (1, 2, 3, 4)
print('%d %d %d %d' % t)

# Test longs
print(0xFFFFFFFFFFFFFFFF)
print(0xFFFFFFFFFFFFFFFF == -1)
print(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
print(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF == -1)

# Test pow
print(pow(2, 31) == 2147483648)
print(pow(2, 32) == 4294967296)
print(pow(2, 63) == 9223372036854775808)
print(pow(2, 64) == 18446744073709551616)

# Test float.hex
print(float.hex(15.9375))
print(float.hex(-15
