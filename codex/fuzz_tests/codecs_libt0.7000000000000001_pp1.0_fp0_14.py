import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
os.system('cls')
print("-" * 60)
print("⚠️  This script will remove all your existent settings ⚠️")
print("-" * 60)

# Delete old config file
if os.path.isfile("settings.txt"):
    os.remove("settings.txt")

# Create config file
f = open("settings.txt", "w")

# Get server name
server_name = input("Server name (default: localhost): ")
if server_name == "":
    server_name = "localhost"

# Get server port
port = input("Server port (default: 80): ")
if port == "":
    port = "80"

# Write config file
f.write("server_name = " + server_name + "\n")
f.write("port = " + port + "\n")

# Close config file
f.close()
