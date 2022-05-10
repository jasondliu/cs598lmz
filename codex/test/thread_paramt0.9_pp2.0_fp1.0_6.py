import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Please press Enter to exit...\n'), daemon=True).start()

# Create an instance of the interface, then run it.
n = NetworkInterface('Debug Interface')
n.run()
n.quit()

# When the interface terminates, wait for any output to complete.
sys.stdout.flush()
