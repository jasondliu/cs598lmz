import codecs
codecs.register_error('strict', codecs.ignore_errors)

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("-t", "--tweetfile", dest="tweetfile", default="twitter.txt",help="file with tweets to be processed")
    argparser.add_argument("-f", "--outputfile", dest="outputfile", default="output.txt",help="output file")
    argparser.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=True,help="turn on verbose mode")
    argparser.add_argument("-q", "--quiet", action="store_false", dest="verbose",help="turn off verbose mode")
    args = argparser.parse_args()
    if args.verbose:
        print("Input file: " + args.tweetfile)
        print("Output file: " + args.outputfile)

    # Parse the tweets
    with open(args.tweetfile) as f:
        data = json
