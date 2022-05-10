import codecs
codecs.register_error("strict", codecs.ignore_errors)

# FIXME: use a logger
def warn(msg):
    print("WARNING: %s" % msg, file=sys.stderr)

def die(msg):
    print("ERROR: %s" % msg, file=sys.stderr)
    sys.exit(1)

def info(msg):
    print("INFO: %s" % msg)

def decode(s):
    return s.decode("utf-8", "strict")

def encode(s):
    return s.encode("utf-8")

def find_files(root, dirs, files):
    result = []
    for name in dirs:
        path = os.path.join(root, name)
        if os.path.isfile(path):
            result.append(path)
    for name in files:
        path = os.path.join(root, name)
        if os.path.isdir(path):
            result.append(path)
    return result

def find_files_rec
