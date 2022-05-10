import signal
signal.alarm(10)

import sys

def read():
    return sys.stdin.readline()

def read_int():
    return int(read())

def read_ints():
    return [int(x) for x in read().split(' ')]

def read_int_map():
    return dict(zip(read_ints(), read_ints()))

def read_int_list():
    return [int(x) for x in read().split(' ')]

def write(s):
    sys.stdout.write(str(s))

def writeln(s):
    write(str(s) + '\n')


def solve(n, m, a, b):
    c = 0
    while n > 0:
        c += 1
        n -= a
        if n > 0 and c % m == 0:
            n += b
    return c


def main():
    (n, m, a, b) = read_ints()
    writeln(solve(n, m, a, b))

