import codecs
codecs.register_error('strict', codecs.ignore_errors) # Make codecs less strict about input files (allows to open files with BOMS)

sys.setrecursionlimit(100000)

# Rewrite sys.argv to be "py" (for testing)
#sys.argv = ["py"]

# If we've installed PyPy as a zip file, use that
if hasattr(sys, 'frozen'):
	sys.path.insert(0, os.path.dirname(os.path.abspath(sys.executable)))


COUNTER = 0
def generate_redirect_filename(filename):
    global COUNTER
    COUNTER += 1
    return "__redirect_output_%s_%d" % (os.path.basename(filename), COUNTER)


def redirect_output(filename):
    sys.stdout.flush()
    if filename:
        try:
            f = open(filename, "w")
        except IOError:
            # Try again with a different filename
            filename = generate_redirect_filename(filename)
            f
