import sys, threading

def run():
    global running
    global th
    global msg
    global msg2

    if running:
        print("Time has already begun")
        return

    running = True

    endTime = time.time() + 60 * 10
    while(endTime > time.time()):
        time.sleep(1)
        msg2.set("Time left: " + str(int(endTime - time.time())))
        root.update()
    running = False

    msg.set("Time is up! Let's start cleaning!")
    msg2.set("Time left: 0")
    root.update()

def start():
    global th
    th = threading.Thread(target=run)
    th.start()

root = tk.Tk()
root.title("Cleaner")

msg = tk.StringVar()
msg2 = tk.StringVar()

label = tk.Label(root, text="Cleaner", width=40)
label.pack()

label = tk.Label(root, textvariable=msg, width=40)
label.pack
