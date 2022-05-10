import types
types.ModuleType('__builtin__').__dict__['_'] = lambda x: x
types.ModuleType('__builtin__').__dict__['N_'] = lambda x: x

#-----------------------------------------------------------------------------
#
# Extract all the messages
#
#-----------------------------------------------------------------------------

def extract_messages(fileobj, keywords, comment_tags, options):
    """Extract messages from GtkBuilder files.

    :param fileobj: the file-like object the messages should be extracted
                    from
    :param keywords: a list of keywords (i.e. function names) that should
                     be recognized as translation functions
    :param comment_tags: a list of translator tags to search for and
                         include in the results
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)``
             tuples
    :rtype: ``iterator``
    """
    tree = etree.parse(fileobj)
    root = tree.getroot()
    if root.tag != 'interface':
        return

    for obj in root.iterchildren
