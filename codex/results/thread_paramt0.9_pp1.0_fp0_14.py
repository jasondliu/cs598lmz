import sys, threading
threading.Thread(target=lambda: httpd.serve_forever()).start()

# Wait for interrupt signal, e.g. KeyboardInterrupt, SystemExit, etc.
while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		print("\nTime to go...")
		sys.exit()

# if __name__ == '__main__':
#     main()
