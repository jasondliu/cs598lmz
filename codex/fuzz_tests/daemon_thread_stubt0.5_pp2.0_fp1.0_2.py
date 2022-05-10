import sys, threading

def run():
    os.system("java -jar ./target/server-1.0-SNAPSHOT.jar")

def main():
    thread = threading.Thread(target=run)
    thread.start()
    os.system("java -jar ./target/client-1.0-SNAPSHOT.jar")

if __name__ == "__main__":
    main()
