import sys, threading

def run():
    if __name__ == "__main__":
        print("[-] that's my job !")
        try:
            while True:
                r = requests.get('https://www.youtube.com')
                print("got response ", r)
                time.sleep(10)
        except (ConnectionError, OSError) as e:
            print(e)

if __name__ == '__main__':
    run()
