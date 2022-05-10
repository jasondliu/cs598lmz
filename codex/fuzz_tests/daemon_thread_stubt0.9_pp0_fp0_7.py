import sys, threading

def run():
    global eng
    global APIID
    global APIKEY
    global SUBJECT
    global MSG
    eng = Engine()

    APIID = sys.argv[1]
    APIKEY = sys.argv[2]
    SUBJECT = sys.argv[3]
    MSG = sys.argv[4]

    eng.start()

def sendMail():
    global APIID
    global APIKEY

    global SUBJECT
    global MSG

    uri = eng.intxdata(APIID,APIKEY,"send", MSG, SUBJECT, None)
    headers = { "Content-type": "application/x-www-form-urlencoded","Accept": "text/plain" }
    conn = httplib.HTTPConnection("sendgrid.com")
    conn.request("POST", uri, urllib.urlencode({}), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    print (data)
    sys.exit()

threading.Thread(target=run).start()
time.sleep(
