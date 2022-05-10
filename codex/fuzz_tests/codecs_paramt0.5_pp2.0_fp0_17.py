import codecs
codecs.register_error('strict', codecs.ignore_errors)

# This is a list of (regular expression, replacement) pairs for abbreviations:
ABBREVIATIONS = [
    (r'(\W)(Dr)(\.)', r'\1\2\3'),
    (r'(\W)(Mr)(\.)', r'\1\2\3'),
    (r'(\W)(Ms)(\.)', r'\1\2\3'),
    (r'(\W)(Mrs)(\.)', r'\1\2\3'),
    (r'(\W)(Jr)(\.)', r'\1\2\3'),
    (r'(\W)(Sr)(\.)', r'\1\2\3'),
    (r'(\W)(St)(\.)', r'\1\2\3'),
    (r'(\W)(Vol)(\.)', r'\1\2\3'),
    (r'(\W)(No)(\.)', r'\1\2\3'),
    (r'(\W)(Rev)(\.)', r'\1\2\
