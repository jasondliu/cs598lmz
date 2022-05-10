import threading
threading.Thread(target=lambda: main_loop()).start()
</code>
So it will run in the background, and be killed if the user asks to exit the program.

