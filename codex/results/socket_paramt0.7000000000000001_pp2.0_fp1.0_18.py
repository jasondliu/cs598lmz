import socket
socket.if_indextoname(3)

# 7 - Write a program that performs an HTTP GET request for the 
#     JSONPlaceholder API for posts made by a user with ID 10.
#     Print the response body to the screen.
import requests
r = requests.get('https://jsonplaceholder.typicode.com/posts/10')
print(r.text)

# 8 - Write a program that connects to the URL http://www.python.org 
#     and prints the HTTP status code.
import requests
r = requests.get('http://www.python.org')
print(r.status_code)

# 9 - Write a program that connects to the URL http://www.python.org 
#     and performs an HTTP HEAD request. Print the response headers.
import requests
r = requests.head('http://www.python.org')
print(r.headers)

# 10 - Write a program that connects to the URL http://www.python.org 
#      and performs an HTTP GET request. Print the response headers.
import requests
r = requests.get('http://www.python.org')
print
