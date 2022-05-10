import codecs
codecs.register_error('oldescape', codecs.escape_decode)

def do(fields):
    if fields[0] in ['->', '<-', '**']:
        return False
    if fields[1].startswith('MGE-'):
        return False
    if fields[3] == '%SLOT%':
        return False
    return True

def isSlot(fields):
    if fields[0] in ['->', '<-', '**']:
        return False
    if fields[1].startswith('MGE-'):
        return False
    if fields[3] == '%SLOT%':
        return True
    return False

def anyFood(fields):
    if fields[0] in ['->', '<-', '**']:
        return False
    if fields[1] == 'FOOD':
        return True
    if fields[1] == 'FOOD_NOWT':
        return True
    if fields[1] == 'FOOD_RAW':
        return True
    return False

def isSleep(fields):
    return fields[
