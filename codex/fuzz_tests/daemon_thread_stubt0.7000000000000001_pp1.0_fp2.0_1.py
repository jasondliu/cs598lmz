import sys, threading

def run():
    os.system("python3 main.py")

def run_bot():
    os.system("python3 bot.py")

def run_web():
    os.system("python3 web.py")

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run_bot)
t3 = threading.Thread(target=run_web)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
