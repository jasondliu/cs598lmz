import sys, threading

def run():
    subprocess.call(["python", "/home/pi/Desktop/project/server.py"])

def read():
    dic = {'status': 'off'}
    #while (dic['status'] == 'off'):
    dic = json.loads(message_paired_phone('on'))
    print dic['status']

def main():
    global t1
    t2 = threading.Thread(target=read)
    t1 = threading.Thread(target=run)
    t1.start()
    t2.start()
    t2.join()
    print('join')
    t1.join()
    print('t1.join')
    while (True):
        pass

if __name__ == "__main__":
    main()
