import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
signal.signal(signal.SIGTERM, signal.SIG_DFL)


def usage():
    print "Reyn: The random source code generator"
    print "Usage:"
    print "reyn.py  [options]"
    print "Options"
    print "  -h, --help\tPrint this help"
    print "  -r, --rlang\tSet source code language"
    print "  -i, --output-asterix\tOutput JSON file for AsterixDB"
    print "  -s, --output-seperate\tOutput each file separately"
    print "  -q, --query\t\tPrint AST of program"
    print "  -l, --limit\tSet number of files to generate"
    print "  -o, --output\tSet output file name"


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "hr:iqls:o:",
