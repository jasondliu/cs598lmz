import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

def get_current_time_in_ms():
    return int(round(time.time() * 1000))
    
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    stop()
    sys.exit(0)

def stop():
    sock.close()

signal.signal(signal.SIGINT, signal_handler)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.settimeout(0.1)

server_address = ('', 7777)
sock.bind(server_address)

# --- SEND ---

def send_packet(command, data=''):
    MESSAGE = bytes(command + data, "utf-
