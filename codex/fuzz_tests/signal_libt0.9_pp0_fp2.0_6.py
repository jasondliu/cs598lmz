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

help="""\
Host and port to send log events to, i.e. 'localhost:8888'"
parser.add_option("-t", "--to", metavar="HOST:PORT",
				  default='localhost:8888', help=help)

opts,args = parser.parse_args()

if not opts.file:
	in_f='/dev/stdin'
else:
    in_f=opts.file

host,port=opts.to.split(':')

if len(args)>0:
	parser.error("unrecognized cmd-line arguments:
