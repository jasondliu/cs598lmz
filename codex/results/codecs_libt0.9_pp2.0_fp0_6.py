import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)


def _print_message(message=''):
    sys.stdout.write(message)
    sys.stdout.flush()

def _get_text_from_user():
    if sys.version_info[0] < 3:
        return raw_input()
    else:
        return input()

def _get_config():
    return open(os.path.join(os.path.dirname(__file__), 'config.json')).read()

def _get_code_from_response(response):
    return response['authorization_code']

def _authorize():
    """Initiates an authorization code grant flow.

    Returns the authorization code URL with which a user can be
    authenticated and granted an authorization code.
    """

    headers = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    data = urllib.parse.urlencode({
        'client
