import threading
threading.Thread(target=lambda: keyboard.wait('alt')).start()

pynput.keyboard.Controller().press(pynput.keyboard.Key.alt)

time.sleep(2)

pynput.keyboard.Controller().release(pynput.keyboard.Key.alt)
