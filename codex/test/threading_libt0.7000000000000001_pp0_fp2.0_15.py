import threading
threading.Thread(target=read).start()

while True:
    for i in range(3):
        x, y = pyautogui.position()
        x = str(x)
        y = str(y)
        print(x + ", " + y)
        data = x + ", " + y
        s.send(data.encode())
    time.sleep(1)
