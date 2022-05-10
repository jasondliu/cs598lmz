import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print ('imdb_sotu_download_and_rename.py -i <inputfile> -o <outputfolder>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('imdb_sotu_download_and_rename.py -i <inputfile> -o <outputfolder>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfolder = arg
    # Read the file first
    file_to_read = open(inputfile, "r")
    lines = file_to_read.read
