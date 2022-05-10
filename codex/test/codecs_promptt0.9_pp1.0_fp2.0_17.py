import codecs
# Test codecs.register_error and the error handling in UnicodeReader.
# Because of our skipping of blank lines in RDRDictReader, some lines
# in the file may have fewer fields than the header.  We register
# our own ReplaceError to force the skipped line to have the same length
# as the header.
import csv
import pkg_resources

def get_data(path):
    '''Get the absolute filename of a file in the data directory.'''
    filename = pkg_resources.resource_filename(__name__, 'data/'+path)
    return filename

class SkipError(Exception):
    pass

def replace(exc):
    extras = exc.args[2]
    return (u'X'*len(extras), exc.start+len(exc.object))

codecs.register_error("replace", replace)

