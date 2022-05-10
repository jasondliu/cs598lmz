import sys, threading

def run():
    while 1:
        print('Python threading with os._exit()')
        sys.stdout.flush()
        time.sleep(5)
        print('Check!')
        sys.stdout.flush()
        time.sleep(5)

threading.Thread(target=run).start()

print('Press any key to exit.')
sys.stdout.flush()
raw_input()

# Force close of all stdio streams
sys.stdout.close()
sys.stdin.close()
sys.stderr.close()

# Exit the interpreter
os._exit(0)
</code>
Result:
<code>Press any key to exit.
Python threading with os._exit()
Check!
</code>
When I replace <code>os._exit()</code> with Python's built-in <code>sys.exit()</code>, the <code>print</code> commands after <code>sys.exit()</code> are still executed.
Replacing <code>os._exit()</code> with <code>os.kill(os.getpid
