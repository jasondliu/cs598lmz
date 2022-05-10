import sys, threading

def run():
    print('run')
    sys.stdout.flush()

    subprocess.check_call(['./test-receive.py', '-t', '1.5'])

threading.Thread(target=run).start()
subprocess.check_call(['./test-send.py', '-t', '1.5'])
