import random
import signal

N = 10000
delays = [1e-6 + random.random() * 2e-5 for i in range(N)]

def handler(signum=None, frame=None):
    if delays:
        signal.setitimer(signal.ITIMER_REAL, delays.pop())
    else:
        print("Done!")

signal.signal(signal.SIGALRM, handler)
handler()
while True: pass
</code>
This program seemed to work fine, but then I decided to play with it, and at some point, the program just got stuck in a loop!
<code>1.6894144538857e-05
1.9072611735187e-05
1.6343771192877e-05
1.9481810824303e-05
1.9150863572227e-05
1.8480385712151e-05
1.9666020890818e-05
1.954099240628e-05
1.632274335976e-05
1.9126768832298e-05
1.9400758029367e-05
1.9746368825742e-05
1.9435212298854e-05
1.96452217
