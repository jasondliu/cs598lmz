import mmap
import os

print(sys.version)

precision = 5
print(f"DEFAULT PRECISION: {precision}")
#print(f"CURRENT PRECISION: {sys.float_info.dig}")
#print(f"MIN NUMBER: {sys.float_info.min}")

"""
def reinterpret_float(value):
    bytes_ = value.to_bytes(8, byteorder='little', signed=False)
    return int.from_bytes(bytes_, byteorder='big', signed=False)

def float_to_hex(value):
    return int(value * (10 ** precision)).to_bytes((precision // 4) + 1, byteorder='big', signed=False).hex()

def hex_to_float(value):
    return int.from_bytes(bytearray.fromhex(value), byteorder='big', signed=False) / (10 ** precision)
"""

def get_bytes(v):
    num_bytes = sys.getsizeof(v)
    #print(num_bytes)
