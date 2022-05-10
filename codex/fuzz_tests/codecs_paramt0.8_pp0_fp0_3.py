import codecs
codecs.register_error('strict', codecs.ignore_errors)


def format_pretty(values, format="%d", **kwargs):
    """Format a list of values into a pretty sentence.

    Parameters
    ----------

        values: list of values to be converted to strings.

        format: format string.

        kwargs: keyword arguments are passed to the format function.
    """
    def format_value(v):
        if isinstance(v, float):
            rounded = int(v) if v == round(v) else v
            return format % rounded
        else:
            return format % v
    if not values:
        return ''
    elif len(values) == 1:
        return format_value(values[0])
    else:
        return '%s and %s' % (', '.join(map(format_value, values[:-1])),
                              format_value(values[-1]))


def format_sentence(s, **kwargs):
    """Formats a string for a human to read.

    Parameters
    ----------

    s: str

