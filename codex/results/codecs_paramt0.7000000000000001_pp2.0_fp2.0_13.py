import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)


def clean_text(text):
    """
    This function removes every non-ascii character
    """
    return text.encode('ascii', 'replace_with_space').decode('ascii')


def clean_html(html):
    """
    This function removes html tags
    """
    html = html.replace("&nbsp;", " ")
    return BeautifulSoup(html, 'html.parser').get_text()


def clean_text_and_html(text):
    """
    This function remove html and non-ascii characters
    """
    return clean_text(clean_html(text))


def clean_text_and_html_and_lower(text):
    """
    This function remove html and non-ascii characters and lower
    """
    return clean_text(clean_html(text)).lower()


def clean_text_and_lower(text):
    """
    This function remove non-ascii characters and lower
    """

