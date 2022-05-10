import socket
+
+def send_command(command):
+    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
+    s.connect(("192.168.1.20", 8080))
+    s.sendall(command.encode())
+    s.close()
+
+def main():
+    parser = argparse.ArgumentParser(description="Send commands to the robot")
+    parser.add_argument("-c", "--command", help="Command to send", required=True)
+    args = parser.parse_args()
+
+    send_command(args.command)
+
+if __name__ == "__main__":
+    main()

