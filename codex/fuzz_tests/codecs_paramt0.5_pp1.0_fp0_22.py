import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

# open files
f = codecs.open(sys.argv[1], 'r', 'utf-8', 'replace_with_space', 'ignore')
fw = codecs.open(sys.argv[2], 'w', 'utf-8')

# read in file
lines = f.readlines()

# make sure we have a header
if len(lines) < 1:
    print 'error: no header'
    sys.exit(1)

# read in the header
header = lines[0]

# split the header
header = header.strip().split('\t')

# make sure we have a header
if len(header) < 1:
    print 'error: empty header'
    sys.exit(1)

# make sure we have a header with a #
if header[0] != '#':
    print 'error: header does not begin with #'
    sys.exit(1)

# make sure we have a header with at least 2 columns
if
