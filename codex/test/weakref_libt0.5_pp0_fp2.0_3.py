import weakref

from namespaces import xmpp


class Element(object):
    """
    An XML element.

    The element has a tag, an optional namespace and a dictionary of
    attributes. It can optionally have a text value.
    """

    def __init__(self, tag, attrib=None, nsmap=None, text=None):
        """
        :param tag: The tag of the element.
        :type tag: unicode
        :param attrib: The attributes of the element.
        :type attrib: dict
        :param nsmap: The namespaces of the element.
        :type nsmap: dict
        :param text: The text value of the element.
        :type text: unicode
        """
        self.tag = tag
        self.text = text
        self.attrib = attrib or {}
        self.nsmap = nsmap or {}

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.tag)

