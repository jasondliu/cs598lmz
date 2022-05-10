import sys, threading
threading.Thread(target=lambda: sys.stdout.write("%s\n" % __loader__.get_filename())).start()

#should return very long string
'''
the string should be:
C:/Users/oqbbshj/Documents/development/eclipse-workspace/threads_and_random/threading_random_gens/src
'''
