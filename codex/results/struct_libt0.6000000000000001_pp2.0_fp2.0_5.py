import _struct

#
# OTA Update
#
def ota_update(host, port, app_name, app_version, app_path):
    print("OTA update: "+host+":"+str(port)+"/"+app_name+"/"+app_version)
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host, port))
    except:
        print("Error connecting to "+host+":"+str(port))
        return False

    try:
        with open(app_path, 'rb') as f:
            try:
                app_data = f.read()
            except:
                print("Error reading app file")
                f.close()
                return False
            f.close()
    except:
        print("Error opening app file")
        return False

    try:
        conn.sendall(b'ota\n')
        conn.sendall(b'name '+app_name.encode('utf-8')+b'\n')
        conn.sendall
