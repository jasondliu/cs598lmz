import socket
import urllib3

ssl._create_default_https_context = ssl._create_unverified_context

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hu:p:o:P:")
    except getopt.GetoptError:
        print('python3 HTTP_Header_Analysis.py -u [url] -p [port] -o [ostype] -P [protocol]')
        sys.exit(2)

    url = None
    port = None
    ostype = None
    protocol = None

    for opt, arg in opts:
        if opt == '-h':
            print('python3 HTTP_Header_Analysis.py -u [url] -p [port] -o [ostype] -P [protocol]')
            sys.exit()
        elif opt in ("-u"):
            url = arg
        elif opt in ("-p"):
            port = arg
        elif opt in ("-o"):
            ostype = arg.lower()
       
