import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(map(str, range(10**6))))).start()
import subprocess
child = subprocess.Popen([sys.executable, "-c", "import time; [time.sleep(0.1) for _ in range(10)]; print('subprocess done')"])
child.wait()

# line_profiler
%lprun -f factorial factorial(20)

# memory_profiler
%mprun -f factorial factorial(20)

# pycallgraph
%load_ext pycallgraph
%pycallgraph
factorial(20)

# tracemalloc
%load_ext tracemalloc
%tracemalloc
factorial(20)

# python -m tracemalloc
# /usr/local/Cellar/python/2.7.12_2/Frameworks/Python.framework/Versions/2.7/lib/python2.7/runpy.py
# import tracemalloc
# /usr/local/Cellar/python/2.7.12_2/
