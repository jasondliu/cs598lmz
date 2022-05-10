import signal
signal.signal(signal.SIGINT, signal_term_handler)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hc:n:",["cidr=","node="])
        if len(opts) == 0:
            raise getopt.GetoptError("No args supplied")
    except getopt.GetoptError:
        print 'ping.py -c <cidr> -n <node>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ping.py -c <cidr> -n <node>'
            sys.exit()
        elif opt in ("-c", "--cidr"):
            cidr = arg
        elif opt in ("-n", "--node"):
            node = arg
    return cidr, node

if __name__ == "__main__":
    cidr, node = main(sys.argv[1:])
    ping(
