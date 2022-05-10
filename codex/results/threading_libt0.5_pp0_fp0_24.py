import threading
threading.stack_size(1024*1024*4)

def main():
    global ws
    ws = websocket.WebSocketApp("ws://localhost:8000/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    main()
