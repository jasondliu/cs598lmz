import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

# The verbosity flag is shared by the options() method of the parser
verbosity = 1

# Global OptionParser object
parser = None

help_message = '''
The following options are supported:
   -h, --help                  show this help message and exit
   -q, --quiet                 print less text
   -v, --verbose               print more text
   -V, --version               print version information and exit
   -f, --file                  read message from this file
   -t, --test                  run self-test
'''

class ParseError(Exception): pass

def error(msg):
    sys.stderr.write('Error: %s\n' % msg)

def int_value(name, opt, value):
    "Store an integer option value."
    try:
        return int(value)
    except ValueError:
        raise ParseError('%s option requires an int value; got %r' %
                         (name, value))

def string_value(name, opt
