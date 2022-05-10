import threading
threading.stack_size(512*2048)
sys.setrecursionlimit(10**8)

def _lambda(loc):
    return (1.0/2)*(1+loc)*(1+loc)
def _mu(loc):
    return (1.0/2)*(1-loc)*(1-loc)
def _sigma(loc):
    return (1.0/2)*(1-loc*loc)

