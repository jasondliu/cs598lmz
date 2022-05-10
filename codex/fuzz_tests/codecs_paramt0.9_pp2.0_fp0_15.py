import codecs
codecs.register_error('strict', codecs.ignore_errors)
import simplejson
import urllib
import urllib2
import httplib

import lindenip
import util
import config
import nameserver

def _post_soap(funcname, soap, host, genserial=True):
    """Helper function for posting to the SOAP API.

    This function exists mostly so that LindenIP.authenticate()
    can reuse the same SOAP post code.

    @return: A response class as returned by util.parse_soap().
    """
    # TODO: use urllib2 to post the data, otherwise we find
    # bogus headers information that mod_security or the
    # php security module or something are sending, which
    # throws off the response headers.
    headers = {"Content-Type": "text/xml; charset=utf-8"}
    if genserial:
        headers["SOAPAction"] = "\"http://api.secondlife.com/%s#%s\"" % (funcname, util.gen_serial32())
    else:
        headers
