import signal
signal.signal(signal.SIGALRM, lambda n, s: exit(-1))
signal.alarm(60)

def bytes2int(bytes):
    return int(bytes.encode('hex'), 16)

def list2int(list):
    return bytes2int(''.join(list))

def getbit(data, index):
    return (data >> index) & 1

def build(data):
    return [True] * data

def update(curr, index, x):
    curr[index] = x
    return curr

def query(curr, indexes):
    return [curr[i] for i in indexes]

def bytes2bool(bytes):
    return [getbit(bytes, i) for i in reversed(range(bytes.bit_length()))]

def bool2str(boolen):
    return ''.join([str(int(i)) for i in boolen])

def bytes2str(bytes):
    return bool2str(bytes2bool(bytes))

def encodeInt(value):
   
