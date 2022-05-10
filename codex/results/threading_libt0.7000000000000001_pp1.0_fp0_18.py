import threading
threading.Thread(target=lambda: keyboard.wait('alt')).start()

pynput.keyboard.Controller().press(pynput.keyboard.Key.alt)

time.sleep(2)

pynput.keyboard.Controller().release(pynput.keyboard.Key.alt)
</code>
Is there any way to make it work?


A:

The issue is that you are sending the key press event before you are ready to listen for it. Change the order of the two sleep calls.
<code>import time
import keyboard
import pynput

threading.Thread(target=lambda: keyboard.wait('alt')).start()

time.sleep(2)

pynput.keyboard.Controller().press(pynput.keyboard.Key.alt)
</code>

