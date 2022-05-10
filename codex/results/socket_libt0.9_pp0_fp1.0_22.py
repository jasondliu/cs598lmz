import socket
import os
import random as random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 80))
s.listen(1)

while(True):
    komm, addr = s.accept()
    while (True):
        data = komm.recv(1024)
        if not data or data=='close':
            komm.close()
            break
        data_arr = data.split("=>")
        angka1 = int(data_arr[0])
        angka2 = int(data_arr[1])
        pesan = data_arr[2]
        if(pesan == "tambah"):
            komm.send("Hasil tambah: %d" % (angka1 + angka2))
        elif(pesan == "kurang"):
            komm.send("Hasil kurang: %d" % (angka1 - angka2))
        elif(pesan == "kali"):

