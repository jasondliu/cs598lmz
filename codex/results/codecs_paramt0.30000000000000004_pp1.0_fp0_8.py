import codecs
codecs.register_error('strict', codecs.ignore_errors)

# ################################################################################################################################

#                                                   ---==={   PARSER   }===---

# ################################################################################################################################

class Parser(object):
    """
    Parser for the .NET Framework.
    """

    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger('zato')
        self.is_verbose = self.logger.isEnabledFor(logging.DEBUG)

    def parse(self, file_path):
        """ Parses a .NET file and returns a dictionary with its contents.
        """
        with open(file_path) as f:
            contents = f.read()

        # We need to remove all comments before we parse the file
        # because otherwise the parser will choke on them.
        contents = self.remove_comments(contents)

        # We also need to remove all empty lines because the parser
        # will choke on them as well.
        contents = self.remove_empty_lines
