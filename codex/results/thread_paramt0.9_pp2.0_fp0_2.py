import sys, threading
threading.Thread(target=lambda:sys.stdout and sys.stdout.flush(),daemon=True).start()

# Which filesystem indexing backend to use? Options:
# - Whoosh:     pure-Python, reasonably robust and featureful, bad index
#               performance and requirements:
#                 - pip install Whoosh
#                 - sudo apt-get install libenchant1c2a
# - Xapian:     good index performance, but has its own requirements and
#               peculiarities:
#                 - pip install xapian-haystack
#                 - sudo apt-get install xapian-tools
#                 - sudo updatedb && xapian-delve `locate ep.db`
#   For more details, see:
#       http://django-haystack.readthedocs.org/en/latest/installing_search_engines.html#whoosh
#       http://django-haystack.readthedocs.org/en/latest/installing_search_engines.html#xapian
HAYSTACK_CONNECTIONS = {
    'default': {
       
