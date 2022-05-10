import sys, threading

def run():
    global reply_received
    global reply_count
    global socket
    global message_count
    global running
    global max_reply_count

    while running:
        reply_received = False
        # Build request
        msg = "request " + str(message_count) + " " + client_name + "\n"
        message_count += 1

        try:
            socket.send(msg.encode())
        except OSError:
            print("Error sending message: " + msg)
            sys.exit(1)

        while not reply_received:
            pass

        reply_count += 1
        if reply_count == max_reply_count:
            break

if len(sys.argv) != 6:
    print("Usage: python3 ping_client.py client_name server_ip server_port max_reply_count delay_between_sends")
    sys.exit(1)

client_name = sys.argv[1]
server_ip = sys.argv[2]
server_port = int(sys.argv[3])
max
