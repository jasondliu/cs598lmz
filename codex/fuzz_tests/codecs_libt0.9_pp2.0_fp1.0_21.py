import codecs
codecs.getreader('utf-8')(f).read()

import json
d = json.load(f)
</code>
Better techniques exist, but the basic idea is that you want the parsing to be done with a codec that understands the character set in which the text is encoded.  Unfortunately, this may not always be possible.  For example, if the decoding fails, one solution is to temporarily change Python's character set so that it matches the character set used by the file being read.  Another is to guess at the text encoding and convert the bytes to a text string using that character set.

