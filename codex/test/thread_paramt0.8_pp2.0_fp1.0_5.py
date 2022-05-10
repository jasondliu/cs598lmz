import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread 2\n')).start()
threading.Thread(target=lambda: sys.stderr.write('Thread 3\n')).start()
 
sys.stdout.write('Main program\n')

#threads = {}
#for i in range(len(tasks)):
#    t = threading.Thread(target=tasks[i], args=(i,))
#    threads[i] = t
#    t.start()

#for i in range(len(tasks)):
#    threads[i].join()

#print('Finished')

#f = open('tmp.log', 'w')
#sys.stdout = f
#print('output...')
#f.close()
