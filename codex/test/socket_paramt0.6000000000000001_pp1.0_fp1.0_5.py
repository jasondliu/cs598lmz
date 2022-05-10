import socket
socket.if_indextoname(3)

import requests

#url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&page=2'
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&page=3'

r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()
print(response_dict.keys())

print("Total repositories:", response_dict['total_count'])

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

print("Selected information about first repository:")

