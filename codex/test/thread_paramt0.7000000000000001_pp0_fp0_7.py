import sys, threading
threading.Thread(target=lambda: (sys.stdout.write(sys.stdin.read()), sys.stdout.flush())).start()

def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def read_str():
    return input()

def read_grid(H):
    '''
    H is number of rows
    '''
    return [input() for _ in range(H)]

def read_match_outcome():
    # Returns 0 if first player won, 1 if second player won or . if draw
    s = read_str()
    if s[1] == '>':
        if s[0] == s[2]:
            return '.'
        else:
            return 0 if s[0] < s[2] else 1
    else:
        if s[0] == s[2]:
            return '.'
        else:
            return 0 if s[0] > s[2] else 1

