import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Ensures encoding/decoding to one that lxml supports.
# It's usually only utf-8 or ascii
def sanitize_lxml_encoding(input_str):
    output_str = input_str
    if isinstance(output_str, str):
        # Encoded as utf-8
        encoding = 'utf-8'
        if is_ascii(input_str):
            # But it is really ascii
            encoding = 'ascii'
        output_str = unicode(input_str, encoding)
    return output_str

# Check if str contains ascii
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Print warning
def print_warning(text):
    print('\n\n\n' + bcolors.FAIL + 'WARNING: ' + bcolors.ENDC + text + '\n\n\n')

# Used for adding information about fixes to meta
def add_to
