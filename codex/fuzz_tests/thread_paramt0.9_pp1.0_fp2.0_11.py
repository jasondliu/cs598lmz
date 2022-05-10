import sys, threading
threading.Thread(target=lambda:web.launch(port=8008)).start()

if __name__ == '__main__':
    address = str(input('Address: '))
    groups = str(input('Address: '))

    app = EmailBomber()
    app.run(address, groups)
    sys.exit()

print('''

Usage:
  - Enter email address to which you would llike to send emails.
  - Enter space seperated list of email to which you would like to send emails.
  (i.e. example1@gmail.com example2@gmail.com example3@gmail.com)
''')
