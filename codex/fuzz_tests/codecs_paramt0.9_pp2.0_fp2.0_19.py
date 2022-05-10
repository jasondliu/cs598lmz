import codecs
codecs.register_error('format', codecs.xmlcharrefreplace)

class Help (BaseDMI.Help):
    """
    DMI help command.  It is easy to subclass dmi.Help for customization.
    
    This help command is used to generate the docstrings below each
    example in the main help file.  You can specify a list of filenames to
    import as
    """
    def __init__ (self):
        super (Help, self).__init__()

        # access to task name, value, docstring
        self.args = []

        # output file
        self.outfile = libcmd_docgen_cfg.getOutput()

        # list of modules to import
        self.import_list = libcmd_docgen_cfg.getImportList()

    def setImport (self, imp_list):
        """
        Set list of modules to import for docs.
        """
        self.import_list = imp_list

    def setOutput (self, outfile):
        """
        Set the output filename.
        """
        self.outfile = outfile

    def set
