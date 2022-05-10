import socket
socket.if_indextoname(3)

# Get the MAC Address
import uuid
mac = uuid.getnode()
print(mac)

# Get local IP
import socket
localIP = socket.gethostbyname(socket.gethostname())
print(localIP)

# Get public IP
import requests
publicIP = requests.get('https://api.ipify.org').text
publicIP = str(publicIP)
print(publicIP)

# Get the country of the public IP
import requests
country = requests.get('https://ipinfo.io/' + publicIP + '/country').text
country = str(country)
print(country)

# Get the city of the public IP
import requests
city = requests.get('https://ipinfo.io/' + publicIP + '/city').text
city = str(city)
print(city)

# Get the region of the public IP
import requests
region = requests.get('https://ipinfo.io/' + publicIP + '/region').text
region = str(region)
print(region)

# Get the postal code of the public
