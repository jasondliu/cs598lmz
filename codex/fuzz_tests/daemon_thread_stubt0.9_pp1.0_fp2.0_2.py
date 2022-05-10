import sys, threading

def run():
    global q_lock
    sys.stdin.readline()
    q_lock = threading.Lock()

threading.Thread(target = run).start()

NUM_WORKERS = int(sys.argv[1])
CLUSTER_SIZE = int(sys.argv[2])
KEY_ID = sys.argv[3]

def tryToClaimLock():
    global q_lock
    if q_lock == None:
        q_lock = threading.Lock()
    q_lock.acquire()

def run_mock_cluster(keyId, testId, clusterId, numWorkers):
    rand = random.Random()
    rand.seed(keyId + " " + testId + " " + clusterId + " " + str(numWorkers))

    time.sleep(rand.randint(0, 200) / 1000)

    for i in range(0, rand.randint(0, 5)):
        tryToClaimLock()
        print("WORKER_ID: " + str(i) + ", clusterId: " + cluster
