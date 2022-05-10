import sys, threading
threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()

# from https://stackoverflow.com/a/16571630/598897
# $ python -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()'

# $ echo "foo" | python -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()'
# foo


# from https://stackoverflow.com/a/16571630/598897
# $ python -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()'

# $ echo "foo" | python -c 'import sys, threading; threading.Thread(target=lambda: sys.stdout.write(sys.stdin.read())).start()'
# foo


# from https://stackoverflow.com/a/1657
