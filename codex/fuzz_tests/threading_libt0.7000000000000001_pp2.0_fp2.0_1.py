import threading
threading.stack_size(67108864) # 64MB stack
# Task definitions.
start_time = time.time()

def do_nothing(context):
    time.sleep(9999999)
    return 'done'

def simple(context):
    time.sleep(0.5)
    return 'done'

def simple_task(context):
    time.sleep(0.5)
    return 'done'

def complex_task(context):
    time.sleep(1)
    return 'complex'

def return_arg(arg):
    time.sleep(0.5)
    return arg

def exception(context):
    raise Exception('thrown error')

def sum_range(context, start, end):
    s = 0
    for i in range(start, end):
        s += i
    return s

def sleep(context, seconds):
    time.sleep(seconds)
    return 'awake'

def sleep_task(context, seconds):
    time.sleep(seconds)
    return 'awake'

def echo(
