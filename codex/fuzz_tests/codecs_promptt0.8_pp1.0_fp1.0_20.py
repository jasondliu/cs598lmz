import codecs
# Test codecs.register_error()

import io
# Test io.TextIOWrapper()

# This file is used to test the "utf-7" codec.

u = [
    'a',
    'Some random text.',

    '\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}',
    'Hi Mom \N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}',
    '\N{ARABIC LETTER ALEF}\N{ARABIC LETTER YEH}\N{ARABIC LETTER ALEF}\N{ARABIC LETTER YEH}',
    '\N{ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM
