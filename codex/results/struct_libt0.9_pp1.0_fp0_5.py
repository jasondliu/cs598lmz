import _struct
import _sre

# Take advantage of Python's own SRE C functions for roles.
FORMAT_STRING_CHARACTERS = (
    _sre.SRE_CODE_CATEGORY_MEMBER, # Name
    _sre.SRE_CODE_IN           , # Width
    _sre.SRE_CODE_IN           , # Precision
    _sre.SRE_CODE_LITERAL_MEMBER, # Literal
    )
FORMAT_STRING_REPEAT_LENGTH = 4


def get_format_string_subexpression_length(records):
    length = 0

    for record in records:
        length += FormatString.parse_subexpression(record.subpatt)[0].count(None)

    return length


def parse_format_string_records(field_length, records, code_scanner):
    # Reference:
    # https://docs.python.org/3/c-api/stdarg.html#id2
    # s = string
    # p = pointers
    # i =
