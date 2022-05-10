import _struct

def check_unsigned_char(value):
    if value < 0 or value > 255:
        raise ValueError("Value %d is not a valid unsigned char." % value)

def check_unsigned_short(value):
    if value < 0 or value > 65535:
        raise ValueError("Value %d is not a valid unsigned short." % value)

def check_unsigned_int(value):
    if value < 0 or value > 4294967295:
        raise ValueError("Value %d is not a valid unsigned int." % value)

def check_unsigned_long_long(value):
    if value < 0 or value > 18446744073709551615:
        raise ValueError("Value %d is not a valid unsigned long long." % value)

def check_signed_char(value):
    if value < -128 or value > 127:
        raise ValueError("Value %d is not a valid signed char." % value)

