import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Todo: make this configurable
# for now, hardcode the files

# Location of the main file
MAIN_FILE = 'cmudict-0.7b.txt'

# Location of the exceptions file
EXCEPTION_FILE = 'cmudict-0.7b.phones'

# Location of the output files
PHONES_OUTPUT = 'cmudict-0.7b.phones'
SYMBOLS_OUTPUT = 'cmudict-0.7b.symbols'

# Location of the temp files
PHONES_TEMP = 'phones.temp'
SYMBOLS_TEMP = 'symbols.temp'

# This is the format of the original file
FORMAT = '%(word)s %(pronunciation)s'

# This is the format of the output files,
# with the first line being the header
OUTPUT_FORMAT = '%(word)s %(phones)s'
OUTPUT_FORMAT_HEADER = 'word phones'

