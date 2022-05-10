import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

def get_data():
    with open("./data/day3.txt") as f:
        return [x.strip() for x in f.read().splitlines()]

def get_lines(data):
    lines = [line.split(',') for line in data]
    return lines

def get_coords(line):
    coords = set()
    x, y = 0, 0
    for move in line:
        direction = move[0]
        distance = int(move[1:])
        if direction == "U":
            for i in range(distance):
                y += 1
                coords.add((x, y))
        elif direction == "D":
            for i in range(distance):
                y -= 1
                coords.add((x, y))
        elif direction == "L":
            for i in range(distance):
                x -= 1
                coords.add((x, y))
