import codecs
# Test codecs.register_error('miegreplace',replace_error)
codecs.register_error('miegreplace',replace_error)

def split_option(s):
    # Split lines that start with the sequence "> " (followed by a space).
    lines = s.splitlines()

    # Remember that the first line has already been stripped.  The
    # stripped() function here returns a *generator* (which is a
    # sequence that doesn't store the elements in memory).  Here it
    # strips each line, including the first one.
    lines = (line.strip() for line in lines)

    # This returns a list consisting of all lines except for the first
    # one, which is the option title.
    opt = [line for line in lines if line]
    return opt

def enumerate_options(text, option_start='---', key_value_pair=':'):
    """
    Parameters:

    - `text`: The string to parse
    - `option_start`: The beginning of a line that introduces an option 
      (by default, '---')
    -
