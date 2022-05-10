import sys, threading
threading.Thread(target=lambda:
    sys.stdout.write( "a bug\n" )).start()

os.system('rm ' + ROOTDIR + '/text/predict/' + filename + '_2.txt')
os.system('rm ' + ROOTDIR + '/text/predict/' + filename + '_5.txt')
os.system('rm ' + ROOTDIR + '/text/predict/' + filename + '_10.txt')
os.system('rm ' + ROOTDIR + '/text/predict/' + filename + '_all.txt')
os.system('rm ' + ROOTDIR + '/text/predict/' + filename + '_all_nocache.txt')

print 'rm ' + ROOTDIR + '/text/predict/' + filename + '_2.txt'
print 'rm ' + ROOTDIR + '/text/predict/' + filename + '_5.txt'
print 'rm ' + ROOTDIR + '/text/predict/' + filename + '_10.txt'
print 'rm ' + ROOTDIR + '/text
