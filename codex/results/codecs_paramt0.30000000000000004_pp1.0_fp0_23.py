import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a list of (regular expression, replacement) pairs for abbreviations:
abbreviations = [
    (r'\b([Cc])o\b', r'\1or'),
    (r'\b([Dd])o\b', r'\1or'),
    (r'\b([Ee])x\b', r'\1x'),
    (r'\b([Ll])b\b', r'\1bs'),
    (r'\b([Mm])a\b', r'\1a'),
    (r'\b([Mm])g\b', r'\1g'),
    (r'\b([Mm])r\b', r'\1r'),
    (r'\b([Mm])s\b', r'\1s'),
    (r'\b([Nn])o\b', r'\1o'),
    (r'\b([Pp])h\b', r'\1h'),
    (r'\b([P
