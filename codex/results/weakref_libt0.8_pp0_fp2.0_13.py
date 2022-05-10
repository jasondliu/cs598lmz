import weakref


def format_html(fmt, *args, **kwargs):
    """
    Syntax sugar for HTML string formatting.

    Allows for concisely formatting strings with lazy-evaluated HTML that
    doesn't need to be escaped or marked safe for templates.

    Examples:

    >>> format_html('<p>{0}</p>', '<i>foo</i>')
    '<p><i>foo</i></p>'

    >>> format_html('<p>{foo}</p>', foo='<i>foo</i>')
    '<p><i>foo</i></p>'

    >>> format_html('<p>{foo}{0}</p>', '<i>foo</i>', foo='<i>Foo</i>')
    '<p><i>Foo</i><i>foo</i></p>'

    >>> format_html('<p>{foo}{0}{bar}</p>', '<i>foo</i>', foo='<i>Foo</i>', bar='<i>bar</
