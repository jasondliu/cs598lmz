import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x55\xaa\x55\xaa\r\n')).start()
threading.Thread(target=lambda: sys.stderr.write('\x55\xaa\x55\xaa\r\n')).start()
end = "\x1b[0m"
while True:
    sys.stdout.write(f"\x1b[38;2;255;255;255m---------------------------{end}")
    line = input("\x1b[34m$\x1b[38;2;255;255;0m ").strip()
    if not line:
        continue
    elif line == "exit":
        exit()
    args = line.split(" ")
    cmd = args[0]
    args = args[1:]
    cmd = "cmd " if sys.platform == "win32" else "bash -c "
    cmd = cmd + f'"{line}" & echo "{end}" & exit & echo "{end}" ' if sys.platform != "win32" else cmd + f'"{line
