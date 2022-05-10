import codecs
codecs.register_error("strict", codecs.ignore_errors)

def get_input_file(inputfilepath):
    infile = None
    try:
        infile = codecs.open(inputfilepath, "r", "utf-8", "strict")
    except Exception as ex:
        print("Failed to open file %s with error: %s" % (inputfilepath, str(ex)))
        infile = None

    return infile

def get_output_file(outputfilepath):
    outfile = None
    try:
        outfile = codecs.open(outputfilepath, "w", "utf-8", "strict")
    except Exception as ex:
        print("Failed to open file %s with error: %s" % (outputfilepath, str(ex)))
        outfile = None

    return outfile

def convert_file(infilepath, outfilepath):
    infile = None
    outfile = None
    try:
        infile = get_input_file(infilepath)
        outfile = get_output_file(
