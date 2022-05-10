import weakref

class GistPlugin(SigSlot):

    def __init__(self, application):
        self.name = 'Gist Plugin'
        self.description = 'Allows you to share the content of your document with others.'
        # self.version = '0.1'
        self.author = 'Mariano Guerra'

        self.application = application
        self.settings = application.get_settings()
        self.files = weakref.WeakValueDictionary()

    def on_document_open(self, document, filename=None):
        """
        Called by the controller when a document is opened into the application.

        :param document: The opened document
        :type document: :class:`~napoleon.document.Document`
        :param filename: The path of the opened document
        :type filename: str
        """
        self.files[document] = document.create_gist()
        self.connect_signals(document)

    def connect_signals(self, document):
        """
        Connect the signals of a document in order to share its content.

        :
