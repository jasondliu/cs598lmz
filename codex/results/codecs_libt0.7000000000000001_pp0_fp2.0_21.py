import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def main(argv):
    # parse command line options
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)
    # process arguments
    for arg in args:
        process(arg) # process() is defined elsewhere

def process(arg):
    print arg

if __name__ == "__main__":
    main(sys.argv[1:])
