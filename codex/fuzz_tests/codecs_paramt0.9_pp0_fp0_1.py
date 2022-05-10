import codecs
codecs.register_error("replace_with_question_mark",
        lambda err: (u"?", err.start + 1))

CHECKS = [
    ["coding", re.compile("coding[=:]\s*([-\w.]+)")],
    ["emacs", re.compile("-\*-\s*([^\*]*?)\s*-\*-")],
    ["vim", re.compile("vim[:=]\s*set\s*([^:]*)")]
]

def check_file(path, encoding=None):
    """
    Check a file path to see what its declared encoding is.

    @param path: C{path} to a file
    @type path: C{str}

    @return: encoding string or None if it can't be declared or isn't valid
    @rtype: C{str}
    """
    if not os.path.exists(path):
        return None

    encoding = encoding or getdefaultencoding()

    try:
        contents = codecs.open(path, "r", encoding).readlines()
