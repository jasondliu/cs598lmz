import codecs
codecs.register_error('strict', codecs.ignore_errors)

# The following two lines are needed to allow Unicode in the console
# (Windows-only)
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

def get_tweets(query, n_tweets=100, max_id=None, lang=None):
    """
    Returns a list of tweets matching a search query.

    Keyword arguments:
    query -- the query string, e.g. "apple"
    n_tweets -- the number of tweets to return (default 100)
    max_id -- returns only tweets with an ID less than (older than) or equal to
              the specified ID (default None)
    lang -- returns only tweets in the specified language (default None)
    """
    params = {'count': n_tweets, 'lang': lang, 'result_type': 'recent'}
    if max_id:
        params['max_id'] = max_id
    response = twitter.get('search/tweets', params=params, verify=
