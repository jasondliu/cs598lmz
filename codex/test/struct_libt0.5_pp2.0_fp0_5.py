import _struct
import math

# Get the data from the file
data = open('data/day10.txt', 'r').read()

# Get the points
points = []
for line in data.splitlines():
    if not line:
        continue

    point = _struct.Point()
    point.x, point.y, point.vx, point.vy = map(int, re.findall(r'[-\d]+', line))
    points.append(point)

# Part 1
# Simulate the points until they converge
seconds = 0
while True:
    # Get the bounding box of the points
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    min_x = min(xs)
    min_y = min(ys)
    max_x = max(xs)
    max_y = max(ys)

    # Get the size of the bounding box
    size = (max_x - min_x) * (max_y - min_y)

    # Move the points
   
