import sys, threading

def run():

while 1:

db_loop()

#using following will cause a crash

#threading.Timer(3600, run).start()

def db_loop():

try:

#do the database stuff

except:

#deal with errors

if __name__ == "__main__":

run()

It can be seen that the timer is commented out. If I uncomment this line, the script will crash. However, if I run the program through the python ide there is no error and the timer runs as normal.

Any ideas?
