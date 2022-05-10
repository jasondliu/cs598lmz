import threading
threading.stack_size(4096*4096)

sentinel = object()
# 推出变量 sentinel
p = multiprocessing.Pool(processes=5)
m = multiprocessing.Manager()
l = m.list([x for x in range(10000)])
d = m.dict()
l_out = m.list()
d_out = m.dict()
def f_init():
    global d
    d = m.dict()
    global l_out
    l_out = m.list()

def f(x):
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

    l_out.append(x)
    return d[x]
# 输出公共变量
def g(l):
    print('l_out', l_out)
    print('d_out', d_out)
