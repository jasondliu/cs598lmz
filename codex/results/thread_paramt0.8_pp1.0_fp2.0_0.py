import sys, threading
threading.Thread(target=lambda: screensaver.prevent_idle(sys.argv[1] if len(sys.argv) > 1 else None)).start()

print 'Preventing idle for', sys.argv[1] if len(sys.argv) > 1 else 'the default time'

while True:
	time.sleep(1)
