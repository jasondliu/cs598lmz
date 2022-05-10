import socket
socket.if_indextoname(3) # get interface name of interface 
socket.if_nametoindex(1) # get interface id of interface 
 
 
 
import urllib2
import urlparse
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib2.install_opener(opener)
urlparse.urljoin('https://www.python.org','about.html') # returns full url
urlparse.urlparse(url) # returns tuple of components of url
urlparse.urlsplit(url) # similar to urlparse but ignores fragment
urlparse.urlunparse(parts) # put parts back together
urlparse.urlunsplit(parts) # put parts back together ignoring fragment
 
 
 
import urllib2
urllib2.unquote('%3F%23%5E%25%26') # reverse escaping
urllib2.quote('abc123()') # url safe
urllib2.quote_plus('abc123()') # url safe with + replacing
