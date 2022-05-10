import threading
threading.stack_size(1024*1024)

# import the Queue class from Python 3
if sys.version_info >= (3, 0):
    from queue import Queue
else:
    from Queue import Queue

# import the urlopen function from the urllib2 module
from urllib2 import urlopen

# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup

# import pprint to print things out in a pretty way
import pprint

# choose a website to crawl
website = "http://www.nytimes.com"

# query the website and return the html to the variable ‘page’
page = urlopen(website)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, "html.parser")

# Take out the <div> of name and get its value
name_box = soup.find('h1', attrs={'class': 'story-heading'})

name = name_box.text.strip() # strip() is used to
