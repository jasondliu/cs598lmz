import threading
threading.Thread.daemon = True

# Be sure to run your tests from the command-line, like the examples below.
#
#   $ python test_your_code.py
#   ...
#   ----------------------------------------------------------------------
#   Ran 1 test in 0.000s
#
#   OK
#
#   $ python test_your_code.py -v  # The -v option shows more detailed info.
#   ...
#   ----------------------------------------------------------------------
#   Ran 1 test in 0.000s
#
#   OK
#   ----------------------------------------------------------------------
#   Ran 1 test in 0.000s
#
#   OK

class TestNewsRelevance(unittest.TestCase):
    def test_news_relevance(self):
        # make sure the news is relevant
        news = News()

        # wait until we get news
        while len(news.get_news()) == 0:
            time.sleep(1)

        # ...and that it's in English (see http://www.i18nguy.com/unicode/language-identifiers.html)
        news_str =
