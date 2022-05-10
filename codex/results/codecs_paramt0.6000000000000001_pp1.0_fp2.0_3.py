import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    """
    main function
    """
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="infile",
                      help="input file", type="string")
    parser.add_option("-o", "--output", dest="outfile",
                      help="output file", type="string")
    parser.add_option("-l", "--lang", dest="lang",
                      help="language", type="string")
    parser.add_option("-c", "--config", dest="config",
                      help="config file", type="string")
    (options, args) = parser.parse_args()
    
    if not options.infile:
        parser.error("input file is required")
    if not options.outfile:
        parser.error("output file is required")
    if not options.lang:
        parser.error("language is required")
    if not options.config:
        parser.error("config file is required")
    
    config = ConfigParser.
