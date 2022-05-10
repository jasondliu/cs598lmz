import signal
signal.signal(signal.SIGTERM, signal.SIG_DFL)#to avoid getting killed by group kill
signal.signal(signal.SIGINT, signal.SIG_DFL)#to avoid getting killed by ctrl-c 

error_count = 0
while 1:
    try:
        if error_count == 60: #errors for 5 minutes
            print str(time.strftime("%H:%M:%S")), "Emailing Log"
            #email_log(STR)
            STR = ""
            error_count = 0
        else:
            resp = urllib2.urlopen(url).read()
            file = open('sample.txt','w')
            resp = resp.decode('utf-8').replace('\t','').replace('\r','')
            file.write(resp) #create temp file for testing response
            file.close() 
            error_count = 0
    except:
        error_count = error_count + 1
        if error_count >= 1:
            print str(time.
