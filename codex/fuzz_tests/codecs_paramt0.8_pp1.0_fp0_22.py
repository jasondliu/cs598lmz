import codecs
codecs.register_error('strict', codecs.ignore_errors)

log = logging.getLogger(__name__)

session = requests.session()


def get_first_header(resp, *names):
    for name in names:
        v = resp.headers.get(name)
        if v:
            return v
    return None


def get_cookies(response):
    cookies = response.cookies
    if not cookies:
        cookie_header = get_first_header(response, 'Set-Cookie', 'Set-cookie')
        if cookie_header:
            cookies = cookiejar_from_dict({})
            cookies.extract_cookies(response.request.response, response.request)
    return cookies


def cookies_to_dict(cookies):
    return dict((cookie.name, cookie.value) for cookie in cookies)


def cookies_from_dict(cookies):
    return cookiejar_from_dict({name: value for name, value in cookies.items()})


def cookies_to_cookie_header(cookies):
    cookie_header =
