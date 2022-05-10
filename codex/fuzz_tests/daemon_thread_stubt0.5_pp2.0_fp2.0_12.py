import sys, threading

def run():
    r = requests.get(sys.argv[1])
    print(r.text)

for i in range(100):
    t = threading.Thread(target=run)
    t.start()
