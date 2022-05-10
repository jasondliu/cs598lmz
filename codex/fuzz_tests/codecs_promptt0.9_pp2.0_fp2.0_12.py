import codecs
# Test codecs.register_error
import modules.test_codecs
import _codecs

# The data is just a string with non-ascii values
data = """Eedåår"""

# Some codecs

codecs = [ ('ascii', 'strict', None),
           ('ascii', 'ignore', None),
           ('ascii', 'xmlcharrefreplace', None),

           ('base64_codec', 'strict', None),
           ('base64_codec', 'ignore', None),
           ('base64_codec', 'replace', None),

           ('binascii', 'strict', None),
           ('binascii', 'ignore', None),
           ('binascii', 'replace', None),

           ('cp037', 'strict', None),
           ('cp037', 'ignore', None),
           ('cp037', 'replace', None),

           ('cp424', 'strict', None),
           ('cp424', 'ignore', None),
           ('cp424', 'replace', None),

           ('cp437', 'strict
