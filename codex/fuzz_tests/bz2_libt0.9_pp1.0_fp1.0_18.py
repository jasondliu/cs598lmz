import bz2
bz2 = bz2.BZ2File('out.dat.bz2')
 
timeSteps = bz2.readline().split('\t')
timeSteps = [ int(x) for x in timeSteps[1:] ]

n = len(timeSteps)

# create array of timeSteps for lookup
timeStepsMap = np.vstack([timeSteps, np.arange(n)]).T

spreads = np.arange(0.5, 10.5, 0.5)
initSize = spreads.size

i = 0
totalBytes = os.path.getsize('out.dat.bz2')

def readSpread(dummy):
    global i, totalBytes
    
    spread = spreads[i]
    print str(i*100.0/initSize) + '%'
    
    f = bz2.readline()
    condition = spreads[i]
    
    i += 1    
    
    print 'read', i, 'entries'
    
    st = np.hstack([spread,
