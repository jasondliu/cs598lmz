import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Python 2/3 cross-compatibility
# Python 3 renamed `raw_input` to `input`
try: input = raw_input
except NameError: pass

# Get the command-line arguments.
try:
  opts, args = getopt.getopt(sys.argv[1:], "hvx:f:")

except getopt.GetoptError as err:
  sys.stderr.write("Error: {0}\n".format(err))
  sys.exit(1)

# Process the command line arguments
verbose = 0
format = "midi"
output = ""
for o, a in opts:
  if o == "-h":
    sys.stdout.write("Usage: midi2json [options]\n")
    sys.stdout.write("Options:\n")
    sys.stdout.write("  -h           Show this help\n")
    sys.stdout.write("  -v           Verbose output\n")
    sys.stdout.write(" 
