import sys, threading
threading.Thread(target=lambda: os.write(1, sys.stdout.buffer.read())).start()

from aocd import data
data = data.splitlines()

def parse_data():
    for line in data:
        line = line.split(' ')
        yield int(line[-3]), line[-2] == 'gain', int(line[-1])

from itertools import permutations, chain
from operator import add, sub
from functools import reduce

def solve(data):
    happiness = dict(parse_data())

    def happiness_change(A, B):
        return happiness[(A, B)] + happiness[(B, A)]

    def happiness_change_all(seating):
        return sum(happiness_change(A, B) for A, B in zip(seating, seating[1:]) + [(seating[-1], seating[0])])

    return max(happiness_change_all(seating) for seating in permutations(happiness))

print(solve(data))
