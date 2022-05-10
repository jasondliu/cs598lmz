import sys, threading

def run():
    print("run")
    sys.exit()

def main():
    print("main")
    threading.Thread(target=run).start()
    print("main")

main()
</code>
Output:
<code>main
run
main
</code>

