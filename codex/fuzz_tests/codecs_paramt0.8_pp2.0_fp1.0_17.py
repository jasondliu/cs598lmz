import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def httpGet(url):
    try:
        urlLib = urllib.urlopen(url)
    except Exception:
        print 'Error: urlLib connection error'
        sys.exit(1)

    try:
        text = urlLib.read()
        code = urlLib.getcode()
    except Exception:
        print 'Error: can not read page'
        sys.exit(1)

    return code, text

def sendMail(subject, text):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(USER, PASS)
        server.sendmail(USER, TO, 'Subject: %s\n\n%s' % (subject, text))
        server.quit()
    except Exception:
        print 'Error: email not sent'
        sys.exit(1)

def main():
    file = open('codigos.txt','r')
    for line in file
