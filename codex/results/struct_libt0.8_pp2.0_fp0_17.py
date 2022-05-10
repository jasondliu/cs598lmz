import _struct

# http://www.howtocrack.com/2012/03/cracking-simple-serial-key-protection.html

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while b != 0:
        (q, a), b = divmod(a, b), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return a, x0, y0

def modinv(a, m):
    a, x, y = xgcd(a, m)
    if a != 1:
        return None
    else:
        return x % m

def lcm(a, b):
    return a * b / gcd(a, b)

def lcmm(*args):
    if len(args) == 2:

