import threading
threading.stack_size(2**30)
sys.setrecursionlimit(10**9)

global T
global seq_lambda, seq

def Vexp(lamb, vold, n):
    v = seq[n]
    vnew = max(v, vold + lamb)
    return vnew

class RerunThread(threading.Thread):
    def __init__(self, seq, n):
        threading.Thread.__init__(self)
        self.seq = seq
        self.n = n
        
    def run(self):
        seq_lambda[self.n] = 0.0
        for v_curr in numpy.arange(seq[self.n] + 1.0, 0.0, -0.01):
            seq_lambda[self.n] = max(Vexp(seq_lambda[self.n], 
                                                v_curr - 0.01, self.n) - v_curr, 0.0)
    
def main():
    global T
    global seq_lambda, seq
    
