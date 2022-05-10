import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

def dec2hex(dec):
    hex = ''
    while dec != 0:
        m = dec % 16
        if m < 10:
            hex += str(m)
        else:
            hex += chr(m - 10 + ord('a'))
        dec /= 16
    return hex[::-1]

def hex2dec(hex):
    dec = 0
    for c in hex:
        dec *= 16
        if c.isdigit():
            dec += ord(c) - ord('0')
        else:
            dec += ord(c) - ord('a') + 10
    return dec

def parse(expr):
    #print 'parse', expr
    expr = expr.lower()
    expr = re.sub('\s', '', expr)
    expr = expr.replace('(', ' ( ')
    expr = expr.replace(')', ' ) ')
    expr = expr.replace(',', ' ')
    expr = expr
