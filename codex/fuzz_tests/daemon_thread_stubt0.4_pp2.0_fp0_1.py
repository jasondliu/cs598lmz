import sys, threading

def run():
    os.system('python3.8 bot.py')

def main():
    while True:
        try:
            threading.Thread(target=run).start()
            time.sleep(1)
        except:
            time.sleep(1)

if __name__ == '__main__':
    main()
