import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#-- Main ----------------------------------------------------------------------
#------------------------------------------------------------------------------

def main():
    """
    Main function.
    """
    #-- Parse command line ----------------------------------------------------
    parser = argparse.ArgumentParser(description = 'Convert a GEDCOM file to a '
                                                   'SQLite database.')
    parser.add_argument('gedcom_file', help = 'GEDCOM file to convert.')
    parser.add_argument('--database', '-d', default = 'gedcom.db',
                        help = 'Name of the SQLite database file.')
    parser.add_argument('--log', '-l', default = 'gedcom.log',
                        help = 'Name of the log file.')
    parser.add_argument('--encoding', '-e', default = 'utf-8',
                        help = 'Encoding of the GEDCOM file.')
    args = parser.parse_args()

    #-- Open the log file -----------------------------------------------------
    log = open(args.log, 'w')

   
