import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello World\n")).start()

# Using subprocess
import subprocess
subprocess.Popen("echo Hello World", shell=True)

# Using multiprocessing
import multiprocessing
multiprocessing.Process(target=lambda: print("Hello World")).start()

# Using os.system
import os
os.system("echo Hello World")

# Using os.popen
import os
os.popen("echo Hello World").read()

# Using os.fork
import os
pid = os.fork()
if pid != 0:
    print("Hello World")

# Using popen2
import popen2
popen2.popen2("echo Hello World")[0].read()

# Using popen3
import popen2
popen2.popen3("echo Hello World")[0].read()

# Using popen4
import popen2
popen2.popen4("echo Hello World")[0].read()

# Using os.spawn*
import os
os.spawnl(os
