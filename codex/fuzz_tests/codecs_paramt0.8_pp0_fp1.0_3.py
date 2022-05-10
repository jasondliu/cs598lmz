import codecs
codecs.register_error("strict", codecs.ignore_errors)


##
##  get file path with extension ftype starting at startfrom, going to curdir
##
def get_file_path(startfrom, ftype, curdir):
    fname = ''
    for root, dirs, files in os.walk(startfrom):
        for file in files:
            if file.endswith(ftype):
                fname = os.path.join(root, file)
                break
        if fname:
            break
    if not fname:
        print 'File not found'
        fname = get_file_path(curdir, ftype, '/')
    return fname


##
##  get initial file, extension is txt
##
COLUMN_SEPARATOR = ":"
COLUMN_SEPARATOR_LEN = len(COLUMN_SEPARATOR)

def get_initial_file(startfrom, ftype, curdir):
    fname = get_file_path(startfrom, ftype, curdir)
    infile = open(f
