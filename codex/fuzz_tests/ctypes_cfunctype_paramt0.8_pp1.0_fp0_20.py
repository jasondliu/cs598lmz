import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_float)

class Point:
    def __init__(self):
        self.x = random.uniform(-1,1)
        self.y = random.uniform(-1,1)

def runif(n):
    return [random.uniform(-1,1) for i in range(n)]

def runifint(n):
    return [int(random.uniform(-1,1)) for i in range(n)]

def disc(p):
    return math.sqrt(p.x**2 + p.y**2) < 1

def hit_or_miss(n):
    hits = 0
    for i in range(n):
        p = Point()
        if disc(p):
            hits += 1
    return 4.0*hits / n

def c_hit_or_miss(n):
    f = FUNTYPE(lib.pi_via_hit_or_miss)
    return f(ctypes.c_float(n))


def monte_carlo(n):
    x = run
