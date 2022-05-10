import threading
# Test threading daemon
import time
# Test time.sleep()
import re
# Test regex

# Import custom modules
import config

# Configure logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def get_http_response(url):
	"""Get the HTTP response for a URL"""

	# Make sure the URL is valid
	if (re.match("^https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$", url)):
		try:
			# Get the HTTP response
			return urllib.request.urlopen(url)
		except Exception:
			# Something went wrong
			logging.error("Could not get response from {}".format(url))
			return None
	else:
		logging.error("Invalid URL provided")
