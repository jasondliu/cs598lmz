import sys, threading

def run():
    c.run("while true; do cat /sys/w1_slave; sleep 1; done")

c.run("modprobe w1-gpio")
c.run("modprobe w1-therm")

with ThreadPoolExecutor(max_workers=1) as pool:
    future = pool.submit(run)

    for line in iter(future.result().stdout.readline, b''):
        print(line)
