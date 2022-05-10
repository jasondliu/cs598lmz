import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\n'.join(map(str, range(10**6))))).start()
import subprocess
child = subprocess.Popen([sys.executable, "-c", "import time; [time.sleep(0.1) for _ in range(10)]; print('subprocess done')"])
child.wait()

# line_profiler
