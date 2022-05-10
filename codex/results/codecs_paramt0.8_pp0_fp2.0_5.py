import codecs
codecs.register_error('strict', codecs.ignore_errors)


class RDFInterface(object):
    """ This class implements an interface for reading and writing RDF data.

        The data is assumed to be encoded in UTF-8.

        Usage:
        with RDFInterface() as transformer:
            transformer.set_input(input_graph)
            transformer.set_output(output_graph)
            transformer.transform(input_format, output_format)

        If transform() is called with input_format = None and output_format = None, the
        data is assumed to be RDF/XML and is only converted to UTF-8.

        Input formats:
        'xml' (RDF/XML), 'turtle', 'n3', 'nt' (N-Triples), 'rdfa'

        Output formats:
        'xml' (RDF/XML), 'turtle', 'n3', 'nt' (N-Triples), 'rdfa'
    """

    def __init__(self):
        """ Initialize internal variables. """

        self.input_graph = None
        self.output_
