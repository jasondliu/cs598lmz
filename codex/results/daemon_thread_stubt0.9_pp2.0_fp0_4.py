import sys, threading

def run():
    url = sys.argv[1:]
    app_id = url[url.index('~')+1:][0]

    while True:
        response = urllib.urlopen(sys.argv[1])
        html = response.read()
        print html
        if '<html' not in html:
            urllib.urlopen('http://alpha.appspot.com/clear?app_id='+app_id)
            break
        time.sleep(2)

thread = threading.Thread(target=run)
thread.start()
