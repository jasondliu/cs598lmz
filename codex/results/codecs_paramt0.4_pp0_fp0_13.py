import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#  "Project" class:
#------------------------------------------------------------------------------

class Project(HasTraits):
    """ A project is a collection of files that can be opened and saved.
    """

    #--------------------------------------------------------------------------
    #  "Project" interface:
    #--------------------------------------------------------------------------

    # The name of the project.
    name = Str

    # The path to the project file.
    path = Str

    # The path to the project directory.
    directory = Property

    # The list of files in the project.
    files = List(File)

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, name, path, files=None):
        """ Initialise the object.
        """
        super(Project, self).__init__()

        self.name = name
        self.path = path
        self.files = files or []

    #--------------------------------------------------------------------------
    #  "Project" interface:
    #--------------------------------------------------------------------------

    def add_file(self, path):
        """ Add a
