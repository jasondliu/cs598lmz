import socket
def isSiteUp(site):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect_ex((site, 80))
        sock.close()
        return True
    except:
        pass
    return False

def take_screen(screen_name = None):
    #screen_name = "checked_data_" + time.strftime("%Y_%m_%d")
    
    my_date = time.strftime('%d.%m.%Y')
    my_time = time.strftime('%H:%M:%S')
    print "Konrol edildiği tarih: " + my_date + " : " + my_time
    
    if(screen_name == None):
        screen_name = "checked_data_" + time.strftime("%Y_%m_%d_%H_%M_%S")
    try:
        os.system('adb shell screencap -
