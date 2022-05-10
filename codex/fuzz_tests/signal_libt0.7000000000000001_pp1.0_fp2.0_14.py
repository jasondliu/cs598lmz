import signal
signal.signal(signal.SIGINT, stop_all)

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    if pressed:
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_move=on_move,
        on_click=on_click) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = Listener(
    on_move=on_move,
    on_click=on_click)
listener.start()

while True:
    time.sleep(1)
    if not listener.running:
        break

listener.stop()
