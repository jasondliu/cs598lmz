import sys, threading

def run():
	print("[*] in run() function")
	command = input("$> ")
	new = command.encode()
	print(new)
	sha1 = hashlib.sha1(new)
	print("[*] Hash: " + sha1.hexdigest())
	t.send("[*] Hash: " + sha1.hexdigest())
	print("[*] Sending: " + command)
	t.send(command)

host = "192.168.128.148"
port = 443

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))

t = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLSv1)

print("[*] Connected to: " + str(host) + " in port: " + str(port) + "\n")
run()

while True:
	cmd
