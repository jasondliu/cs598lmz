import sys, threading
threading.Thread(target=lambda:sys.stdout.write('')).start()

# I/O
INPUT_FILE_NAME = 'B-small-attempt0'
#INPUT_FILE_NAME = 'B-large'
#INPUT_FILE_NAME = 'sample'
#OUTPUT_FILE_NAME = 'output'

# Open input files
try:
    in_file = open(INPUT_FILE_NAME + '.in', 'r')
    #out_file = open(OUTPUT_FILE_NAME + '.out', 'w')
except:
    print ('Error opening files!')
    sys.exit()

def next_line():
    return in_file.readline().strip()

def next_int():
    return int(next_line())

def next_ints():
    return [int(x) for x in next_line().split(' ')]

def next_float():
    return float(next_line())

def next_floats():
    return [float(x) for x in next_line().split(' ')]

def next_list():
