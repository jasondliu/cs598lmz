from types import FunctionType
list(FunctionType(f.__code__, {}, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

list(module_paths(functions=False, classes=True, modules=False, exceptions=False))


########################################################################################################################

import multiprocessing as mp

def listener(q):
    '''listens for messages on the q, writes to file. '''

    f = open('mp_log.log', 'w')
    while 1:
        m = q.get()
        if m == 'kill':
            f.write('#killed')
            break
        f.write(m + '\n')
        f.flush()

def logger(q, level_name, msg):
    q.put('%s:%s' % (level_name,msg))

q = mp.Queue()
listen_p = mp.Process(target=listener, args=(q,))
listen_p.start()

#logger(q, 'debug', 'asdf')
#log
