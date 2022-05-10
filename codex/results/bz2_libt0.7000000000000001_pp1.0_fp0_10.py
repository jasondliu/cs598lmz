import bz2
bz2.compress("test")

import time
for i in range(5):
    time.sleep(0.5)
    print("test")

import subprocess
p = subprocess.Popen("python -m timeit -n 10 -s 'import test' 'test.test()'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, errors = p.communicate()
print(output, errors)

import multiprocessing
def worker():
    for i in range(5):
        time.sleep(0.5)
        print("test")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker)
    p.start()
    print("multiprocessing")
