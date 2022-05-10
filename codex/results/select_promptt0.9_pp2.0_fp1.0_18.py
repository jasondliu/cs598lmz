import select
# Test select.select for edge-triggered behavior.
#
# If evdev kernel driver is used, this test will hang as it will
# incorrectly put select(evdev, ...) into level-triggered mode.

import evdev
import select
import time

# Find a suitable input device
def find_dev(nr):
    d = None
    while True:
        try:
            d = evdev.InputDevice('/dev/input/event' + str(nr))
        except FileNotFoundError:
            nr += 1
        if d is not None:
            return d

d = find_dev(1)

d.grab()

start = time.time()

while True:
    r, w, x = select.select([d], [], [d], 2)

    if r:
        print("select(d, [], []) returns: %s" % r)
    if x:
        print("select(d, [], []) returns: %s" % x)

    elapsed = time.time() - start
    print('%-3.3f'
