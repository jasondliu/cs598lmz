import signal
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

#
# top-level script environment
#
parser = OptionParser(version="%prog: $Id$")

#
# Arguments
#
help="""\
Filename to read logger stream, or STDIN if omitted."""
parser.add_option("-f","--file", metavar="FILE", default='', help=help)

