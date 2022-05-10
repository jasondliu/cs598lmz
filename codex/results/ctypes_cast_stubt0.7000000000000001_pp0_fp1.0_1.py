import ctypes
ctypes.cast(buffer, ctypes.POINTER(ctypes.c_int64))[0]

def int64_to_bytes(value):
    return value.to_bytes(8, byteorder='big')


def int64_to_bytes(value):
    return value.to_bytes(8, byteorder='big')


def int64_from_bytes(value):
    return int.from_bytes(value, byteorder='big')


def uint64_to_bytes(value):
    return value.to_bytes(8, byteorder='big', signed=False)


def uint64_from_bytes(value):
    return int.from_bytes(value, byteorder='big', signed=False)


def int128_to_bytes(value):
    return value.to_bytes(16, byteorder='big')


def int128_from_bytes(value):
    return int.from_bytes(value, byteorder='big')


def uint128_to_bytes(value):
    return value.to_bytes(16, byteorder='big', signed=False)
