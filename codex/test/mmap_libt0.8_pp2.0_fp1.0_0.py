import mmap
import re
import os
import sys
import array

WIDTH = 100
HEIGHT = 40

# Define empty grid
GRID = []
for i in range(HEIGHT):
    GRID.append([0] * WIDTH)

# Load initial configuration
startx = int(sys.argv[2])
starty = int(sys.argv[3])
endx = int(sys.argv[4])
endy = int(sys.argv[5])
f = open(sys.argv[1], "r")

i = 0
for line in f:
    j = 0
    for nb in re.findall('\d+', line):
        GRID[i][j] = int(nb)
        j += 1
    i += 1

f.close()
