import threading
threading.Thread(target=webserver).start()

tap0 = netifaces.ifaddresses('tap0')
myip = tap0[netifaces.AF_INET][0]['addr']

# Main loop
