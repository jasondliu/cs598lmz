import threading
threading.stack_size(4096*4096)

start = time.time()

# ===================================================================
minsup = 10
learners = {} # node -> {tr => frq}
frqsingletons = {}

def countsin(k, tx, lx):
    # sort transactions
    tx.sort()
    tmp = 0
    cnt = []
    for i in range(k):
        tmp += tx[i]
        cnt.append(tmp)
    
    tups = []    
    for i in range(lx-k+1):
        t = ()
        for j in range(k):
            t += (tx[i+j],)
        tups.append([t,cnt[i+k-1]-cnt[i]])

    return Counter(tups)

def count(t, tx, lx):
    # sort transactions
    tx.sort()

    bc = []
    singletons = []

    tmp = 0
    cnt = []
    k = len(t)
    for i in range(k
