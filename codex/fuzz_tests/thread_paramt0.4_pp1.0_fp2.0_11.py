import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

# import sys, time
# for i in range(100):
#     sys.stdout.write('\r%d' % i)
#     sys.stdout.flush()
#     time.sleep(0.1)

# import sys, time
# for i in range(100):
#     sys.stdout.write('\r%d' % i)
#     sys.stdout.flush()
#     time.sleep(0.1)
# print('\n' * 100)

# import sys
# sys.stdout.write('\x1b[2J\x1b[H')
# print('\n' * 100)

# import sys, time
# for i in range(100):
#     sys.stdout.write('\x1b[2J\x1b[H')
#     sys.stdout.write('%d' % i)
#     sys.stdout.flush()
#     time.sleep(
