import socket                                         

s = socket.socket()          
print("Socket successfully created")                           
port = 12345                
s.bind(('', port))         
print("socket binded to %s" %(port))    
s.listen(5)      
print("socket is listening") 
while True:
    c, addr = s.accept()      
    print('Got connection from', addr)
    s_ip=addr[0]
    from datetime import datetime
    timestamp=str(datetime.now())
    timestamp=timestamp[0:20]
    data=c.recv(1024)
    data=str(data)
    split_data=data.split(":")
    if(split_data[0]=="timestamp"):
        import sqlite3
        conn = sqlite3.connect('attendance.db',check_same_thread=False)
        with conn:
            cursor = conn.cursor()
            #inserting or updating row in table 
