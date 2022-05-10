import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

class Authorize(object):
  def GET(self):
    """Get an authorization token to get access to Playlist API."""
    request = oauth.OAuthRequest.from_request("GET",
                                              "http://audio.search.yahoo.com/OAuth/V1/get_request_token",
                                              headers={"Authorization": "OAuth realm=\"http://audio.search.yahoo.com/OAuth/V1\""})

    _consumer = oauth.OAuthConsumer(CONSUMER_KEY, CONSUMER_SECRET)
    request.sign_request(oauth.OAuthSignatureMethod_PLAINTEXT(), _consumer, None)

    conn = httplib.HTTPConnection("api.login.yahoo.com")

    conn.request(request.http_method, request.to_url())
    response = conn.getresponse()
