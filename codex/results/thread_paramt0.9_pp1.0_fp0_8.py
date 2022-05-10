import sys, threading
threading.Thread(target=lambda: sys.stdout.write("WA\n")).start()
sys.exit(42)
"""


CONTEST_HOST = 'localhost'
CONTEST_PORT = 9999

def connect_to_contest(u, p, ret=False):
    s = socket.socket()
    try:
        s.connect((CONTEST_HOST, CONTEST_PORT))
    except Exception as e:
        print("Fail to connect to service")
        sys.exit(1)
    s.send(json.dumps({'username': u, 'password': p}).encode() + b'\n')
    # print("connect_to_contest1")
    data = s.recv(4096).decode()
    # print("connect_to_contest2")
    # print(data)
    d = json.loads(data)
    if not d['success']:
        print(d['message'])
        sys.exit(1)

    if ret:
        return s
    s.close()

sh = socket.socket(socket.AF
