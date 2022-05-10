import mmap
import sys

def send_recv(data):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(('localhost', 9000))
    conn.send(data)
    conn.setblocking(0)
    try:
        return conn.recv(1024)
    except:
        return None

def test_basic(data):
    print "Testing Basic Case"
    print "Request:\n", data
    response = send_recv(data)
    print "Response:\n", response
    print "-"*50

def test_vuln(data, vuln_pos):
    print "Testing Vulernable Case"
    print "Vuln Position:", vuln_pos
    print "Request:\n", data
    response = send_recv(data)
    print "Response:\n", response
    print "-"*50

def test_newline_trick(data):
    print "Testing Newline Trick Case"
    print "request:\n", data
    response = send_recv
