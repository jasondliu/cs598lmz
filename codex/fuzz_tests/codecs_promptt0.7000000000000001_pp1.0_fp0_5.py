import codecs
# Test codecs.register_error()

import codecs, string

test_cases = [

    # Test  XML character entities
    ('&amp;', '&'),
    ('&apos;', "'"),
    ('&gt;', '>'),
    ('&lt;', '<'),
    ('&quot;', '"'),

    # Test HTML character entities
    ('&nbsp;', u'\u00A0'),
    ('&iexcl;', u'\u00A1'),
    ('&cent;', u'\u00A2'),
    ('&pound;', u'\u00A3'),
    ('&curren;', u'\u00A4'),
    ('&yen;', u'\u00A5'),
    ('&brvbar;', u'\u00A6'),
    ('&sect;', u'\u00A7'),
    ('&uml;', u'\u00A8'),
    ('&copy;', u'\u00A9'),
    ('&ordf;', u'\u00AA'),

