import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()
end
</code>
Hopefully this works sufficiently well for you. 

