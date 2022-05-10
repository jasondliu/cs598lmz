import threading
threading.stack_size(67108864)
start=time.time()

def mempool(mempool,transactions,miners,blks,avglength):

    newmempool=[]
    status=[]
    for i in range(len(transactions['transaction'])):
        if transactions['transaction'][i][0]<=transactions['transaction'][transactions['newmemorigin'][i]]['timestamp']:
            status.append(1)
        else:
            status.append(0)
    for i in range(len(transactions['transaction'])):
        if status[i]==0:
            newmempool.append(i)

    mempool=list(set(mempool)-set(newmempool))
    unconfirmedmempool=transactions['transaction'][mempool]
    save = copy.deepcopy(unconfirmedmempool)
    unconfirmedmempool=sorted(unconfirmedmempool, key=lambda k: k['amount'], reverse=True)
    count=0

    N=miners['power']
