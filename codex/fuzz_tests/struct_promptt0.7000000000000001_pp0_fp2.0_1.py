import _struct
# Test _struct.Struct and Format

def get_integer(k):
    return random.randint(-2**31, 2**31-1)

def get_long(k):
    return random.randint(-2**63, 2**63-1)

def get_float(k):
    sign = 1
    exp = random.randint(0, 255)
    if random.choice([0, 1]):
        sign = -1
    if exp == 0:
        exp = random.randint(1, 255)
    else:
        exp -= 127
    man = random.randint(0, 0xffffffff)
    if man == 0:
        man = random.randint(1, 0xffffffff)
    return sign * (1 + float(man) / 0x100000000) * 2.0**exp

def get_double(k):
    sign = 1
    exp = random.randint(0, 2047)
    if random.choice([0, 1]):
        sign = -1
    if exp == 0:
        exp = random.randint(1
