import codecs
codecs.register_error("strict", codecs.ignore_errors)

# -----------------------------------------------------------------------------
# Classes:
# -----------------------------------------------------------------------------

class Base(object):
    """Abstract base class for all Hachoir parsers.

    Fields are stored in the "root" instance attribute.
    """

    # Default endianess (use LITTLE_ENDIAN or BIG_ENDIAN)
    endian = LITTLE_ENDIAN

    # Name of the parser (ex: "Jpeg image")
    static_size = None
    PARSER_TAGS = { }

    # List of children (ex: list of JPEG segments)
    CHILDREN = { }

    # List of fields to display
    DISPLAY = [ ]

    # List of fields to edit in graphical interface
    EDITABLE = [ ]

    # List of fields to print
    PRINTABLE = [ ]

    # List of fields to save in a XML file
    XML_ATTRIBUTES = [ ]

    # List of fields to export
    EXPORT = [ ]

    # List of fields to filter (ex: list of JPEG markers)
    FIL
