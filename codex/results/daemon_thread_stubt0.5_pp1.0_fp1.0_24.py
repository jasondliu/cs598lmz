import sys, threading

def run():
    ftp = ftplib.FTP(sys.argv[1])
    ftp.login(sys.argv[2], sys.argv[3])
    ftp.cwd(sys.argv[4])
    ftp.storbinary('STOR ' + sys.argv[5], open(sys.argv[6], 'rb'))
    ftp.quit()

threading.Thread(target=run).start()
