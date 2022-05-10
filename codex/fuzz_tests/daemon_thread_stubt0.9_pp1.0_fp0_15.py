import sys, threading

def run():
  server = xmlrpc.client.ServerProxy("http://localhost:8000/")
  print("3 is even: %s" % str(server.is_even(3)))
  print("100 is even: %s" % str(server.is_even(100)))

t = threading.Thread(target=run)
t.start()
</code>

