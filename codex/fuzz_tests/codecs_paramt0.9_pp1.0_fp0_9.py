import codecs
codecs.register_error("mrescape", codecs.escape_decode)


def _assert_no_unicode_on_windows():
    if os.name == "nt":
        assert not any(isinstance(arg, unicode)
                       for arg in sys.argv[1:])


def parseoptions(argv, opts):
    """Parse the given command line options.

    Return a dictionary with the options found.
    Return the list with the non-option arguments left.
    """
    result = {}
    args = []
    if 'hgcmds' in __all__:
        result["hgcmds"] = []
    argv = argv[1:]
    while argv:
        a = argv.pop(0)
        if not a.startswith('-'):
            if 'hgcmds' in __all__:
                result["hgcmds"].append(a)
            elif opts:
                args.append(a)
            else:
                args.append(a)
            continue
        if len(a) > 1 and
