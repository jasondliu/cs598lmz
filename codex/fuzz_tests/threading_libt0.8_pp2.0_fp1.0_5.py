import threading
threading.Thread(target=server.serve_forever).start()
'''

class Utilities:


	def __init__(self):
		pass


	def send_data(self, src, dest, data, headers={}):
		try:
			#print("Source: " + src + " Dest: " + dest + " Data: " + data)
			# Sends a POST request to the specified URL
			# Package the data, add some headers, and post it 
			headers['IP-Address'] = socket.gethostbyname(socket.gethostname())
			headers['Source-Address'] = src
			headers['Destination-Address'] = dest
			headers['Data-Length'] = len(data)
			
			data = urllib.parse.urlencode(data).encode("utf-8")
			request = urllib.request.Request(dest, data, headers)
			response = urllib.request.urlopen(request)
			response
