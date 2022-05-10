import sys, threading

def run():
    import os
    import subprocess

    # Create the FIFO
    os.mkfifo(sys.argv[1])

    # Open the FIFO and wait for some input
    with open(sys.argv[1], "r") as f:
        while True:
            msg = f.readline().strip()

            # If we get a message, try to launch the URL
            if msg != "":
                subprocess.Popen(["xdg-open", msg])

threading.Thread(target=run).start()
