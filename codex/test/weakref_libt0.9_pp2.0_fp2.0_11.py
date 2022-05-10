import weakref
from CrawlInternet import CrawlInternet
from CrawlDbPedia import CrawlDbPedia
from CrawlYoutube import CrawlYoutube


class Crawler(object):
    '''
    classdocs
    '''


    def __init__(self, parameters=None):
        '''
        Constructor
        '''
#         parameters = {
#                       'place': 'punchbowl',
#                       'query': '2421 Punchbowl St.',
#                       'state': 'Hawaii',
#                       'county': 'Honolulu',
#                       'url': 'http://www.zillow.com/homes/2421-Punchbowl-St.,Honolulu,HI,96822_rb/',
#                       'zipcode': 96822,
#                       'status': 'for sale',
#                       }        
        if parameters:            
            self.parameters = parameters
                        
    def crawl(self):
        
        return self.wikipedia(self.parameters)
        
