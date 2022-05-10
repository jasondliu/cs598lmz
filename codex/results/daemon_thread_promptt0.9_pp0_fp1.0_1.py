import threading
# Test threading daemon threads rather than normal ones.
# These shut down when the function returns.
daemons = 1
# Time-wait interval between loading requests.
url_poll_interval = 1.0

def thread_function(user_key, profile_url_list):
# -----------------------------------------------------
	"""Given a list of URLs, create a profile object and load each of the URLs into it."""
	profile = profile.Profile(user_key)
	for url_num in profile_url_list:
		url = "%s%d" % (url_base, url_num)
		profile.get(url)
		time.sleep(url_poll_interval)
		print("url ("+url+") loaded.")


def main():
# ----------
	"""Function's docstring"""
	profile_url_list = range(0, url_top)

	# Create a dictionary of (key, value) pairs, one for each user to be loaded.
	# The key is used to store and retrieve the profile at the end of the test.
	# The value is a list of the URL numbers
