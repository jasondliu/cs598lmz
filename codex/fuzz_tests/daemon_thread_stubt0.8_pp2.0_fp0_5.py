import sys, threading

def run():
    print("running")
    subprocess.check_call(['xdg-open', 'http://127.0.0.1:8080/'])
    server = SimpleXMLRPCServer((sys.argv[1] if len(sys.argv) > 1 else ""), 8080)
    server.register_introspection_functions()
    server.register_function(get)
    server.serve_forever()

def get(path):
    if path.startswith("/"):
        path = path[1:]
    rdir = os.path.dirname(os.path.realpath(__file__))
    rpath = os.path.join(rdir, path)
    if os.path.exists(rpath):
        with open(rpath, "rb") as f:
            content = base64.b64encode(f.read()).decode()
        return {
            "path": path,
            "status": "ok",
            "content": content,
            "isFile": os.path.isfile(r
