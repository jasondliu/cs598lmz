import threading
threading.Thread(target=lambda: os.system('python3 -m http.server --cgi')).start()

import cgi
import cgitb; cgitb.enable()

print("Content-type: text/html\r\n\r\n")
print("""
<html>
<head>
<title>Hello World - First CGI Program</title>
</head>
<body>
<h2>Hello World! This is my first CGI program</h2>
""")

form = cgi.FieldStorage()

if "name" in form:
    name = form["name"].value
    print("<h1>Hello %s!</h1>" % name)

print("""
</body>
</html>
""")
