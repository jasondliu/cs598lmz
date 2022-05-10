import sys, threading

def run():
    while True:
        line = sys.stdin.readline()
        if line == 'get\n':
            image = capture_image()
            image.save(sys.stdout, 'JPEG')
            # Make sure that there is a newline at the end of the message.
            print('')
            sys.stdout.flush()
        elif line == 'exit\n':
            print('exit')
            t._Thread__stop()
            break

def capture_image():
    return Image.open('capture.jpg')

t = threading.Thread(target=run)
t.daemon = True
t.start()
t.join()
