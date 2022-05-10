import sys, threading

def run():
	server_address = ('127.0.0.1', 8080)
	httpd = HTTPServer(server_address, CORSRequestHandler)
	print('Starting httpd on port 8080...')
	httpd.serve_forever()

def main():
	thread = threading.Thread(target=run)
	thread.daemon = True
	thread.start()
	
	# Open browser
	webbrowser.open('http://127.0.0.1:8080/index.html')
	
	while True:
		x = raw_input("Please enter something")
		print("You entered: " + x)
		
if __name__ == "__main__":
	main()
