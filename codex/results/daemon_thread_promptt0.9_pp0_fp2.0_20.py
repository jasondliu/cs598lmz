import threading
# Test threading daemon

def myfunc():
    '''
    define function for testing purpose, does nothing but printout statements in loop
    :return:
    '''
    while True:
        print("Ciao Ciao Ciao")
        time.sleep(1)

thread =threading.Thread(target=myfunc)
thread.daemon = True
thread.start()


# Test URL request stub

#def get_req(url):
#    print('\n************************')
#    print(url)
#    print('************************\n')
#
#urls = ['http://www.google.com','http://www.bbc.com','zetcode.com','http://www.example.com/']
#for u in urls:
#    get_req(u)
