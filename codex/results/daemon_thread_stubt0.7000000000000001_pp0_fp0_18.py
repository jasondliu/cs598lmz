import sys, threading

def run():
    while True:
        main()
        time.sleep(30)

def main():
    db = dbm.open('db', 'c')
    try:
        if sys.platform == 'win32':
            db['last'] = str(os.stat('data.csv').st_mtime)
        else:
            db['last'] = str(os.stat('data.csv').st_mtimespec)
    finally:
        db.close()

if __name__ == '__main__':
    threading.Thread(target=run).start()
