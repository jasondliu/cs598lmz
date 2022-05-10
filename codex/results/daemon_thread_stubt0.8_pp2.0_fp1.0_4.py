import sys, threading

def run():
    try:
        r = requests.get('http://localhost:8080/v1/1_0/sample')
        print r.status_code
        print r.text
    except Exception as e:
        print e

if __name__ == '__main__':
    print 'Start'
    thread_list = []
    for i in range(300):
        t = threading.Thread(target=run)
        t.daemon = True
        thread_list.append(t)
    for i in thread_list:
        i.start()
    while threading.activeCount() > 2:
        pass
    print 'All Done'
