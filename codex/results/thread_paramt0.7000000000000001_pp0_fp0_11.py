import sys, threading
threading.Thread(target=lambda:sys.stdout.write(get_ipython().kernel.blobs['my_token'].decode('utf-8'))).start()

!pip install pygithub
from github import Github
g = Github(get_ipython().kernel.blobs['my_token'].decode('utf-8'))

import requests
import getpass
from github import Github

# First create a Github instance:

# using username and password
g = Github("user", "password")

# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)


# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_
