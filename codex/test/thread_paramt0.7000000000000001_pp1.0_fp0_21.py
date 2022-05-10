import sys, threading
threading.Thread(target=lambda: sys.stdin.readline()).start()

from collections import defaultdict
from queue import Queue

from intcode import IntCode

# Read input
program = list(map(int, sys.stdin.readline().split(',')))

# Part 1
def part1(program):
    ic = IntCode(program)
    ic.run()
    return ic.outputs[0]

# Part 2
def part2(program):
    ic = IntCode(program)
    ic.set_inputs([2])
    ic.run()
    return ic.outputs[0]

print("Part 1: %s" % part1(program))
print("Part 2: %s" % part2(program))
