import socket
import urllib
import time
import re

BANNER = """
             __    __                    ______
__  ______  / /___/ /___  __  ______  / ____/___  ________
/ / / / __ \/ / __  / __ \/ / / / __ \/ /   / __ \/ ___/ _ \\
/ /_/ / /_/ / / /_/ / /_/ / /_/ / / / / /___/ /_/ / /  /  __/
\____/\____/_/\__,_/ .___/\__,_/_/ /_/\____/\____/_/   \___/
                 /_/

"""

class GoBuster:

	def __init__(self, url, cookies, extensions, file_list, out_file, verbose, thread_number, recurse, dot_file_list, auth, kwargs):
		self.url = url
		self.cookies = cookies
		self.extensions = extensions
		self.file_list = file_list
	
