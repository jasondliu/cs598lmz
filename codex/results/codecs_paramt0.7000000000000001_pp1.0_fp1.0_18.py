import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

# RE_COMMENT_MARKER - a regular expression that checks for the presence of a comment
# marker in a source line
RE_COMMENT_MARKER = re.compile(r"^[\t ]*([\#;]|--).*$")

# RE_COMMENT_START - a regular expression that checks for the presence of a comment
# start marker in a source line.
RE_COMMENT_START = re.compile(r"^[\t ]*/\*.*$")

# RE_COMMENT_END - a regular expression that checks for the presence of a comment
# end marker in a source line.
RE_COMMENT_END = re.compile(r"^.*\*/[\t ]*$")

# RE_COMMENT_INSIDE - a regular expression that checks for the presence of a comment
# inside a source line.
RE_COMMENT_INSIDE = re.compile(r"/\*.*\*/")

# RE_EMPTY_LINE
