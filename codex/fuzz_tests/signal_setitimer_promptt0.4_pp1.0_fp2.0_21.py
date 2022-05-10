import signal
# Test signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)

# import time
# import resource
# import os
# import sys

# def handler(signum, frame):
#     print "handler"
#     print resource.getrusage(resource.RUSAGE_SELF)
#     print resource.getrusage(resource.RUSAGE_CHILDREN)

# def main():
#     signal.signal(signal.SIGPROF, handler)
#     signal.setitimer(signal.ITIMER_PROF, 0.1, 0.1)
#     while True:
#         time.sleep(1)

# if __name__ == "__main__":
#     main()

# import time
# import resource
# import os
# import sys

# def handler(signum, frame):
#     print "handler"
#     print resource.getrusage(resource.RUSAGE_SELF)
#     print resource.getrusage(resource.RUSAGE_CHILDREN)

#
