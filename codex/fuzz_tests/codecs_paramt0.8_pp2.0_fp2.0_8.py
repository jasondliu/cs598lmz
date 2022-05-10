import codecs
codecs.register_error('strict', codecs.ignore_errors)

def log(message):
    print "ppx: "+message

def ppx_parse(filename, cache_dir):
    log("opening file %s" % filename)
    with codecs.open(filename, encoding="utf8", errors="strict") as f:
        log("reading file %s" % filename)
        lines = f.readlines()
        log("splitting into lines")
        lines = [l.rstrip() for l in lines]
        log("removing comments")
        lines = [l for l in lines if not l.startswith("#")]
        log("creating set of meaningful lines")
        ppx_lines = set([l.partition("#")[0].rstrip() for l in lines if l])
        log("done")

        return ppx_lines

def ppx_check(filename, ppx_lines, cache_dir):
    log("opening file %s" % filename)
    with codecs.open(filename, encoding="utf8", errors="strict") as f
