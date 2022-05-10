import sys, threading
threading.Thread(target=lambda: sys.stdout.write('threading\n')).start()
threading.Thread(target=lambda: sys.stdout.write('threading\n')).start()

# threading.Thread(target=lambda: sys.stdout.write('threading\n'), daemon=True).start()
# threading.Thread(target=lambda: sys.stdout.write('threading\n'), daemon=True).start()

# threading.Thread(target=lambda: sys.stdout.write('threading\n')).start()
# threading.Thread(target=lambda: sys.stdout.write('threading\n')).start()

from multiprocessing import Process

# def run():
#     print('multiprocessing')
#
# p = Process(target=run)
# p.start()
# p.join()
#
# p = Process(target=run)
# p.start()
# p.join()
#
# p = Process(target=run)
# p.daemon = True
# p.start()
# p
