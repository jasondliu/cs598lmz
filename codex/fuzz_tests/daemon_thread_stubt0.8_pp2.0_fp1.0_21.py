import sys, threading

def run():

print "Starting " + threading.current_thread().getName()

sys.stdout.flush()

thread = threading.Thread(target=run, name="test")

thread.setDaemon(True)

thread.start()

print "done!"

thread.join()

print "exiting"

sys.stdout.flush()



print "done!"

thread.join()

exiting

done!



print "done!"

thread.join()

Starting test

exiting

done!



Python 3.3.3

threading

threading.Thread

Not sure what is the best way to reproduce this, but it seems to be something like this:On my Linux machine (Ubuntu, Python 2.7.5) I am getting:which is exactly what I expect.On Windows 7 machine (Python 2.7.5) I am getting:Do you have any idea what is going wrong on my Windows machine?EDIT: Python 3.3.3 behaves similarly:Linux:Windows:EDIT2: Windows seems to be alright now (I
