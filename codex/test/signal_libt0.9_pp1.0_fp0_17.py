import signal
signal.signal(signal.SIGINT, signal_handler)

def send_data(sock, message):
  try:
    sock.sendall(message)
  except socket.error:
    print("Error in sending data, socket has been closed")

def recv_data(sock):
  try:
    data = sock.recv(1024)
  except socket.error:
    print("Error in reading data, socket has been closed")
  return data

def main():
  global client_socket

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.settimeout(2)

  parsing = argparse.ArgumentParser("Networking Client")
  parsing.add_argument("-ip", help="Ip address")
  parsing.add_argument("-p", "--port", help="Port number")
  args = parsing.parse_args()

