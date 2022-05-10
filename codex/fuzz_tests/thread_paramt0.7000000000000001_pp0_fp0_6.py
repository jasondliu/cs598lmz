import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()
</code>
This is a quick and dirty way to clear the screen and move the cursor to the top-left corner.
It uses the same escape sequence that your terminal would use when you press ctrl-l.

