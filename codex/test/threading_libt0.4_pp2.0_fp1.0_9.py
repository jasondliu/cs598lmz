import threading
threading.stack_size(67108864)

def get_input():
    return sys.stdin.readline().strip()

def get_input_int():
    return int(get_input())

def get_input_array():
    return get_input().split(' ')

def get_input_int_array():
    return [int(x) for x in get_input_array()]

def get_input_float_array():
    return [float(x) for x in get_input_array()]

def get_input_float():
    return float(get_input())

def get_input_long():
    return long(get_input())

def get_input_long_array():
    return [long(x) for x in get_input_array()]

def get_input_char_array():
    return [char for char in get_input()]

def get_input_char():
    return get_input()[0]

def get_input_string():
    return str(get_input())

