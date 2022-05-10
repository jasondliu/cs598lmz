import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# Primeiro script
# cat t.txt | python3 a.py | python3 b.py | python3 c.py | python3 d.py
