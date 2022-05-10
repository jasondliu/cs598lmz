import codecs
codecs.getreader('utf8')(sys.stdin)

# find the capital of a given country
def find_capital(country):
    """
    Returns the capital of a given country.

    The function finds the capital of a country using the CIA World Factbook
    data.

    Parameters
    ----------
    country : string
        Name of the country.

    Returns
    -------
    capital : string
        Name of the capital of the country.

    Notes
    -----
    The input country name must be the same as the one in the CIA World Factbook.
    The function does not resolve synonyms, e.g. 'United States' and 'USA'.
    This function does not work for South Sudan!

    Examples
    --------
    >>> find_capital('Germany')
    'Berlin'
    >>> find_capital('Sweden')
    'Stockholm'
    >>> find_capital('Nepal')
    'Kathmandu'
    """
    # open the URL and parse the HTML-formatted data
    url_template = 'https://www.cia.gov/library/publications
