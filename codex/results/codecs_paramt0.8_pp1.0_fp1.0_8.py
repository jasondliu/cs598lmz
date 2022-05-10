import codecs
codecs.register_error("strict", codecs.replace_errors)

def _main(argv, environ):
    args, rest = getopt.getopt(argv[1:], "hb:c:f:", ["help", "base=", "config=", "config-file="])
    if not args:
        print >> sys.stderr, __doc__
        return 1
    base = "."
    config = []
    for opt, val in args:
        if opt in ("-h", "--help"):
            print >> sys.stderr, __doc__
            return 0
        elif opt in ("-b", "--base"):
            base = val
        elif opt in ("-c", "--config"):
            config.append(val)
        elif opt in ("-f", "--config-file"):
            config.append((open(val, "rb"), val))

    # load config file(s)
    cfg = ConfigParser()
    cfg.readfp(codecs.getreader("utf-8")(StringIO('
