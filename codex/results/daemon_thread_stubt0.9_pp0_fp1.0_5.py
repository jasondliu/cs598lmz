import sys, threading

def run():
    args = sys.argv
    argc = len(args)
    if argc >= 2:
        if args[1] == '1':
            microftp.ftpServer()
        elif args[1] == '0':
            if argc == 3:
                microftp.ftpClient(args[2])
            else:
                print('Usage: microftp_ex.py 0 <filename>\n(<filename> is the filename to initiate a ftp.)')
    else:
        print('Usage: microftp_ex.py <server=1 or client=0> <filename=optional>\n')

if __name__ == '__main__':
    args = sys.argv
    run()
