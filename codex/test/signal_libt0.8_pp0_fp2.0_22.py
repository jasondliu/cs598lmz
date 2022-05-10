import signal
signal.alarm(20)

for i in range(1000):
    print(i)
    sleep(.001)

print("Done")
