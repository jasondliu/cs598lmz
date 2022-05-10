import threading
threading.Thread(target=start).start() 
print "\n"
print "Server is running on port 5000"

# Close the server when the application is closed
while 1:
    time.sleep(1)
