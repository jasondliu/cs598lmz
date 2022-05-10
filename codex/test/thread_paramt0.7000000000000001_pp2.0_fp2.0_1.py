import sys, threading
threading.Thread(target=lambda: sys.stdout.write('i am a threading\n')).start()

import datetime
from datetime import date
from datetime import time
from datetime import datetime

def main():
    today = datetime.now()
    print("the current date and time is ", today)

    t = datetime.time(datetime.now())
    print("the current time is ", t)

if __name__ == '__main__':
    main()
