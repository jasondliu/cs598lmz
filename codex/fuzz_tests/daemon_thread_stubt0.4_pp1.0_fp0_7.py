import sys, threading

def run():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    for i in range(5):
        sys.stdout.write('\033[0;0H')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.write('\033[2K')
        sys.stdout.
