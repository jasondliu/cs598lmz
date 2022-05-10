import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()
def print_lines(lines):
    for line in lines:
        print '\r\x1b[K' + line,
        sys.stdout.flush()
        time.sleep(.1)
    print

while True:
    print_lines(["  1","  2","  3","  4","  5","  6","  7","  8","  9","  10","  11","  12","  13","  14","  15","  16","  17","  18","  19","  20","  21","  22","  23","  24","  25","  26","  27","  28","  29","  30","  31","  32","  33","  34","  35","  36","  37","  38","  39","  40","  41","  42","  43","  44","  45","  46","  47","  48","  49","  50","  51","  52","  53","  54","  55","  56
