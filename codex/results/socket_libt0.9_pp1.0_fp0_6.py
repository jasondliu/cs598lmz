import socket
 
from M2Crypto import SSL, httpslib, Err, m2urllib

#=========================================================================

class SSLTest:
    """A simple HTTP client to test the SSL classes.

    This is a very basic HTTP client that uses the M2Crypto SSL classes
    to do HTTP/1.0 requests.  It implements as few functions as possible
    to demonstrate how to use the SSL classes and get some decent
    results.
    
    It will currently do HTTP/1.0 requests, including GET and HEAD,
    authenticating using either Basic or Digest authentication.
    If a proxy is used it will send the HTTP connect via the proxy.

    It will print the HTTP response headers and the body.  The
    body is printed only if there was a successful HTTP command and
    the body has at least 32k in it.  This is to keep this class
    from printing a Transfer-Encoded chunked body for GET commands
    that have no body """

    def __init__(self, host, port=0, ssl_port=443, proxy=None,
                 username=None, password=None,
