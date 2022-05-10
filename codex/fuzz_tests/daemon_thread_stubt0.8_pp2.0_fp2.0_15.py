import sys, threading

def run():
    def f(p, *args, **kwargs):
        print(p, args, kwargs)
        return p + sum(args) + sum([kwargs[x] for x in kwargs])
    
    def test(p):
        return f(p, 1, 2, 3, a=1, b=2, c=3)

    t0 = time.clock()
    for i in range(1000000):
        test(5)
    t1 = time.clock()
    print(t1 - t0)


threading.Thread(target=run).start()
