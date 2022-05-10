import sys, threading

def run():
    for n in range(100):
        print("Hello")

thread = threading.Thread(target=run)


print("Start")
thread.start() # Start thread
print("End")

# Start
# End
# Hello
# Hello
# Hello
# ...


def run2(name, n):
    for i in range(n):
        print(name)

for n in range(20):
    thread = threading.Thread(target=run2, args=(f"Thread{n}", 3))
    thread.start()

# Thread10
# Thread3
# Thread12
# Thread14
# Thread16
# Thread9
# Thread18
# Thread19
# Thread0
# Thread1
# Thread2
# Thread4
# Thread5
# Thread6
# Thread7
# Thread8
# Thread13
# Thread11
# Thread15
# Thread17
# Thread12
# Thread9
# Thread3
# Thread14
# Thread16
# Thread18
# Thread19
# Thread0
# Thread1
# Thread2
# Thread4
