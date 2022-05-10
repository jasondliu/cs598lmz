import threading
threading.stack_size(2**28)

def _init_():
    global _global_dict
    _global_dict = {}
    file_name = os.path.splitext(os.path.split(__file__)[1])[0]
    pid = os.getpid()
    f = open('/tmp/{0}_{1}.lock'.format(file_name, pid), 'w')
