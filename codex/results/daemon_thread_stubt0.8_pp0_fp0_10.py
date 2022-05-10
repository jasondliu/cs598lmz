import sys, threading

def run():
	os.system("python3 websocket-client.py")

while True:
    if __name__ == "__main__":
        for i in range(8):
            thread = threading.Thread(target=run)
            thread.deamon = True
            thread.start()

"""
