import codecs
codecs.register_error('strict', codecs.ignore_errors)

class RedirectException(Exception):
  pass

class Site:

  _u = urllib.FancyURLopener()
  _html_parser = HTMLParser()
  _re_redirect = re.compile('^\s*<(head|script)>\s*(<meta http-equiv="refresh" \w+=".*")</{0,1}?(head|script)>\s*$')
  _cookiejar = cookielib.CookieJar()
  _cookiejar.set_policy(cookielib.DefaultCookiePolicy(rfc2965=False))
  _u.addheaders.append(('User-Agent', 'Mozilla/5.0 (X11; U; SunOS x86_64; en-US; rv:1.9) Gecko/20090221 Firefox/3.0'))
  _u.addheaders.append(('Cookie', 'PHPSESSID=2063f3b76e9f87d866c22cee1bdd8f
