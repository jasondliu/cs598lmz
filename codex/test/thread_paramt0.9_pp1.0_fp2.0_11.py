import sys, threading
threading.Thread(target=lambda:web.launch(port=8008)).start()

if __name__ == '__main__':
    address = str(input('Address: '))
    groups = str(input('Address: '))

    app = EmailBomber()
    app.run(address, groups)
    sys.exit()

