import codecs
codecs.register_error("strict", codecs.ignore_errors)
logger = log.setup_custom_logger("dslparsing")

class Resource_parser:
    def __init__(self):
        pass

    def parse(self, uri):
        if uri.endswith(".xml") and (not uri.endswith("capabilities.xml")):
            return self.parse_xml(uri)
        else:
            raise e.ResourceNotValid("The provided resource is not valid")


    def _wrap_uri(self, uri):
        if "://" not in uri:
            uri = "http://" + uri
        return uri


    def parse_xml(self, uri):
        uri = self._wrap_uri(uri)
        mechanism = check_mechanism(uri)
        handler = self._get_handler(uri, mechanism)
        valid_objs = handler(uri)

        if not valid_objs:
            raise e.ResourceNotValid("The provided resource is not valid")

        return valid_objs
