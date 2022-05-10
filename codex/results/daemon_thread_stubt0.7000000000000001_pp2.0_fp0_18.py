import sys, threading

def run():
    #print "Thread started"
    c = Client()
    c.run()

def main():
    print "Starting client..."
    global cont
    cont = 1
    #print "Thread started"
    c = Client()
    c.run()


if __name__ == "__main__":
    main()
