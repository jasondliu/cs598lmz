import sys, threading
threading.Thread(target=lambda:sys.stdout.write('<p>Too many connections...')).start()
"""
server.mount('/',hug.get(on_invalid=on_invalid))
debugger = hug.middleware.debugger.install(server)

def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--debug', dest="debug", action="store_true", default=False, help="runs in debug mode")
    parser.add_argument('-H','--host', dest="host", default="127.0.0.1", help="listen for specific host")
    parser.add_argument('-p','--port', dest="port", type=int, default=5000, help="listen for specific port")
    return parser.parse_args()

if __name__ == '__main__':
    args = command_line()
    server.run(
        host=args.host, 
        port=args.port,
        debug=args.debug,
        use_reloader=False
    )
