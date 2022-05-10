import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
def read_file(filename, ignore_errors=False):
    '''
    Reads the contents of a file.

    @param filename: The name of the file to read.
    @param ignore_errors: If true, decoding errors are ignored.
    @return: The file contents.
    '''
    try:
        # Open the file.
        f = open(filename, 'r')
        contents = f.read()
        f.close()
    except:
        # Could not read the file.
        contents = ''
    if not ignore_errors:
        return contents
    else:
        # Ignore decoding errors.
        return contents.decode('utf-8', 'strict')

#------------------------------------------------------------------------------
def write_file(filename, contents):
    '''Writes the given contents to the file.'''
    f = open(filename, 'w')
    f.write(contents)
    f.close()

#------------------------------------------------------------------------------
def read_properties(filename):
    '''
    Reads
