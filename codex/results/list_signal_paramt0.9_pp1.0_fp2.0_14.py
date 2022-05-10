import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())


nnn = []
signal.signal(signal.SIGALRM, handler)
def kkk(x):
    nnn.append(x)

def fff(x):
    return x
for i in range(N/1000):
    yy = {}
    for i in range(1000):
        delays.append(i)
    handler()
    if i % 10 == 0:
        print 'i'

print len(nnn)

nnn = set(nnn)
nnn = list(nnn)

vv, kv = np.histogram(nnn, bins=50)

print vv
print kv

plt.plot(kv[1:], vv, '+')
plt.show()
