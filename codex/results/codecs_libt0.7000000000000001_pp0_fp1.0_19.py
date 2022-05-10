import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_page(page_name, revision=False):
    """
    This function gets the page content of a page in the wiki

    :param page_name: The name of the page to be retrieved
    :param revision: If you want the latest revision of the page, set it to False
    :return: The contents of the page
    """
    if revision:
        r = requests.get('https://wiki.mozilla.org/api.php?action=query&prop=revisions&format=json&rvprop=content&titles=' + page_name)
        try:
            return r.json()['query']['pages'].values()[0]['revisions'][0]['*']
        except KeyError:
            return None
    else:
        r = requests.get('https://wiki.mozilla.org/api.php?action=parse&format=json&page=' + page_name)
        try:
            return r.json()['parse']['text']['*']
