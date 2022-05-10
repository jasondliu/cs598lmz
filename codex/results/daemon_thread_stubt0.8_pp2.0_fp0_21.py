import sys, threading

def run():
    print "Connected!"

    while True:
        data = s.recv(1024)
        i = 0
        while i < len(data):
            c = data[i]
            if c == '#':
                return
            i += 1
        sys.stdout.write("\x08 \x08")
        sys.stdout.flush()
        sys.stdout.write("%d/%d" % (i, len(data)))
        sys.stdout.flush()

def mf():
    print "Connected!"

    while True:
        data = s.recv(1024)
        if data:
            sys.stdout.write(data)
            sys.stdout.flush()
        else:
            break


if __name__ == '__main__':

    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help
