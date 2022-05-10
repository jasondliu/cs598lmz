import select
# Test select.select() by setting a timeout.
# Don't need to use an fd, but what the heck, it's ambiguous without something.
# This example should eventually return timeout.
ins, outs, exs = select.select([0], [], [], 2.5)
print("select = %r" % ins)

def alarm(time):
    def handler(signum, frame):
        print("alarm")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

alarm(5)
time.sleep(2)
print("no alarm yet")
ins, outs, exs = select.select([0], [], [], 2.5)
print("select = %r" % ins)

def ala(time):
    def handler(signum, frame):
        print("alarm")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

ala(10)
print("no alarm yet")
ins, outs, exs = select.select([0], [], [
