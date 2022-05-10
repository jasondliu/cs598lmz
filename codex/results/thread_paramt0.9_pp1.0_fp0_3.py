import sys, threading
threading.Thread(target=lambda: sys.exit(1)).start()
print("This line should appear before the exit of the thread.")
</code>
Which I think is a fairly common misconception. I'm not sure if I see any easy solutions to this.
    

