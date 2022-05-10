import codecs
codecs.register_error('strict', codecs.ignore_errors)

class FileSystemLoader(BaseLoader):
    """Loads templates from the file system.  This loader can find templates in
    folders on the file system and is the preferred way to load them.  To
    load templates from the file system, create the loader with the
    path to the templates as string, or a list of paths to look for
    templates in:

    .. sourcecode:: python

        >>> loader = FileSystemLoader('/path/to/templates')

    Per default the template encoding is ``'utf-8'`` which can be changed by
    setting the `encoding` parameter to something else.

    .. versionchanged:: 2.7
       The `encoding` parameter was added.

    .. versionadded:: 2.4
       The `followlinks` parameter was added.

    :param searchpath: the path to the templates.
    :param encoding: the encoding of the templates.
    :param followlinks: set to `True` if symlinked directories should be
                        followed.
    """

    def __init__(self, searchpath, encoding='
