import sys, threading

def run():
    subprocess.run(["python", "-m", "http.server", "8182"])

print("Starting server...")
t = threading.Thread(target=run)
t.start()

time.sleep(1)
print("Connecting to server...")

c = chievo.Chievo(chi_addr="wss://localhost:8182")

@c.add_event("event1")
def handle_event1(event):
    print("Got event \"event1\".")
    if event.args["arg"] == "hello":
        c.send_event("event2")

c.add_event("event2", c.print_event)
c.add_event("event4", c.print_event)

time.sleep(2)

print("Sending...")

c.send_event("event1", arg="hello")

print("Sent!")

print("\nPress any key to exit...\n")
input()
