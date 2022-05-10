import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import random

def rand_int():
    return random.randint(0, 255)

def rand_color():
    return (rand_int(), rand_int(), rand_int())

def rand_pos(width, height):
    return (random.randint(0, width), random.randint(0, height))

def rand_size():
    return random.randint(10, 50)

def rand_shape():
    choice = random.randint(0, 2)
    if choice == 0:
        return 'rectangle'
    elif choice == 1:
        return 'circle'
    else:
        return 'triangle'

def rand_rotation():
    return random.randint(0, 360)

def rand_point(x, y, width, height):
    return (random.randint(x, x + width), random.randint(y, y + height))

def rand_points(x, y, width,
