import threading
threading.stack_size(1000000)

def chunks(l, n): # this is used for every 100 rows of longs
    for i in range(0, len(l), n):
        yield l[i:i + n]

def conv_group_to_long(group):
    time_list = list(map(lambda x : str(x), group))
    return int("".join(time_list))

def conv_group_to_time(group):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(group))

def gen_delta_time_list(fin, fout):
    """
    Given time list will convert each to int and add the diff with previous
    """
    time_list = []
    for line in fin:
        time_list.append(line.strip())

    time_list = list(map(lambda x : int(x), time_list)) # convert to int
    prev = None
    for t in time_list:
        if prev is None:

