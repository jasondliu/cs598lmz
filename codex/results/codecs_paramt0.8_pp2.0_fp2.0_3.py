import codecs
codecs.register_error('ucn', codecs.replace_errors)

# This is based on the Google Python module with some modifications
# http://code.google.com/p/google-api-python-client/

# More helpful urls:
# https://developers.google.com/console/help/#service_accounts
# https://developers.google.com/accounts/docs/OAuth2ServiceAccount
# https://developers.google.com/drive/web/scopes
#
# 1. Follow the instructions here to create a project and client ID:
#    https://developers.google.com/drive/web/auth/web-server
# 2. Download the JSON file and put it in the same directory as your code.
# 3. Rename it to "client_secrets.json".
# 4. The scope URL is:
#       https://www.googleapis.com/auth/drive
#    All of the other ones listed on that page are optional.

import urllib
from oauth2client.client import SignedJwtAssertionCredentials
from oauth2client.client
