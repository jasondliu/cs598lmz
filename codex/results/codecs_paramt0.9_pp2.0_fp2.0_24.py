import codecs
codecs.register_error(codecs.lookup_error('utf-8'), replace_with_question)

# This is a work-around for a strange problem with Unicode parsing that I can't
# figure out. For example, if there's a sequence of two utf-8 words that starts
# with 0x80, then the parser considers it a binary file.
# For example, (in hex) "00 80 00" is valid utf-8, so it's a binary file,
# but "00 00 80" is valid utf-8, so it's not binary.
# I don't understand what it is. When I turn on "python -v", the stack trace is
# the same for each case, so it must be something dumb, like the way that popen
# or a module it uses parses the system calls.
# Anyway, the fix is to turn on binary mode. Rather than change ALL the lexers,
# I'll change the ones that are problematic.
#
# FIXME: What is the real fix?
def open_for_read(path):
  path = path.replace('\%', '%')
  try
