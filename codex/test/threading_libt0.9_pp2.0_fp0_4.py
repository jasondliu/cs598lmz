import threading
threading.stack_size(67108864)


def gettime(): return str(datetime.datetime.now())


niter = 100000
msg_len = 32
ddir = '/tmp/'
npb = 11
nrs = 25
tunit = 'sec'


# Initialisation function
def initializer(arg1, arg2):
    global npblk, nranks, ddir, rq
    npblk = arg1
    nranks = arg2
    ddir = ddir + str(nranks) + 'ranks/'
    if not os.path.isdir(ddir):
        os.mkdir(ddir)
    rank = MPI.COMM_WORLD.Get_rank()
    rq = []
    for i in range(nranks):
        rq.append([])
    mf = ddir + 'masterfile_' + str(rank)
    os.system('rm '+mf+'*.*')


def sender():
    # Send
    rank = MPI.COMM_WORLD.Get
