import select
def main():
    inputs = [sys.stdin]
    outputs = []
    message_queues = {}
    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)
        for s in readable:
            if s is sys.stdin:
                message = sys.stdin.readline()
                message = message.strip('\n')
                if message == "quit":
                    inputs.remove(s)
                    break
                if message.split(" ")[0] == "server":
                    try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.setblocking(0)
                        s.connect((message.split(" ")[1], int(message.split(" ")[2])))
                        inputs.append(s)
                        message_queues[s] = Queue.Queue()
                    except:
                        print("Connection Error")
            else:
                try:
                    data = s.recv(1024)
                    if not data:
                        print("Disconnected from server")
