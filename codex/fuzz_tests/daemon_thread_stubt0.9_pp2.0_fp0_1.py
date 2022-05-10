import sys, threading

def run():
    print "Hello! My name is Jesus."
    while True:
        print "I'm the Son of God."

if len(sys.argv) == 2:
    for trait in sys.argv:
        if trait == 'son_of_god':
            print "Receiving title from command line arguments, I am the Son of God"
        else:
            print "There are no other command line arguments available."
            print "Please enter 'son_of_god'"
            break

if threading.active_count() == 1:
    who_am_i = threading.Thread(target=run)
    who_am_i.start()
