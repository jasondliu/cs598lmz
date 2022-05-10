import socket
import subprocess

def get_mac(ip_address):
    response = subprocess.Popen(["arp", "-n", ip_address], stdout=subprocess.PIPE).communicate()[0]
    mac_index = response.index(" at ")
    mac = response[mac_index+4: mac_index+21]
    return mac


def ipscan(start_ip, end_ip):
    state = []
    while start_ip != end_ip:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            s.connect((start_ip, 135))
            s.send(b'GET STACK OVERFLOW')
            result = s.recv(1024)
            if result:
                mac = get_mac(start_ip)
                state.append({'host' : start_ip, 'mac' : mac})
        except Exception as e:
            print('.', end=' ')
