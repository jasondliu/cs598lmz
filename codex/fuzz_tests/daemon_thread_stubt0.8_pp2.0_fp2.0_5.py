import sys, threading

def run():
    print("start")
    # cmd = 'timeout ' + str(timeout) + 's ' + 'nmap -sV --script "http-vuln-*" -Pn -oX result/' + url + '.xml -p ' + str(
    #     port) + ' ' + url
    # cmd = 'timeout ' + str(timeout) + 's ' + ' nmap '+url
    cmd = ' nmap -sV  -Pn  -p 80 -oX result/' + url + '.xml ' + url
    print(cmd)
    result = os.popen(cmd)
    print(result.read())
    print("end")

timeout = 20
# port = '80'
port = '80'
url = '127.0.0.1'

if __name__ == '__main__':
    threading.Thread(target=run).start()
