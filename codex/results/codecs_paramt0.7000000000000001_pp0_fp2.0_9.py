import codecs
codecs.register_error('ignore_invalid_hex', codecs.ignore_errors)

def get_valid_filename(s):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot.
    >>> get_valid_filename("john's portrait in 2004.jpg")
    'johns_portrait_in_2004.jpg'
    """
    s = force_unicode(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)

def get_hexdigest(algorithm, salt, raw_password):
    """
    Calculate the HMAC-SHA1 of 'raw_password' with 'salt' using the specified
    algorithm ('md5', 'sha1' or 'crypt').

    If 'raw_password' is None then a random salt will be generated (you can use
    get_random_string() to generate the salt).

