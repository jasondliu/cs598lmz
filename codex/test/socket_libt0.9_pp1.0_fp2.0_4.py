import socket
import time

# tm=time.strftime("%H:%M:%S",time.localtime(time.time()))
# print tm
#print ukmedia.DescapeHTML( s )
#print time.strftime("%Y-%m-%d %a %H:%M:%S",time.localtime( time.time() ) )
# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime( time.time()))
# print time.strftime("%a, %d %b %Y %H:%M:%S +0000",time.gmtime())

###################################################################################################

import urlparse

def build_absolute_url( base_url, url ):
	return urlparse.urljoin( base_url, ukmedia.DescapeHTML(url) )

###################################################################################################

def GetFetcher():
	return IndependentFetcher()

