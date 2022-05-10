import sys, threading

def run():
	sys.stdout.write("Infinite loop!\n")
	while True:
		pass

def stop():
	sys.stdout.write("Terminating program!\n")
	threading.Thread(target=sys.exit, args=(0,)).start()

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == 'stop':
		stop()
	else:
		run()
```

### On MacOS
This script uses the hotkey feature of Keyboard Maestro to provide system interrupt.

Default key is `Cmd` + `Ctrl` + `Shift` + `x`

This script tries to stop all python programs by sending the os-interrupt signal to the interpreter thread.

### On Windows
This script uses the keyboard hook feature of pynput to provide system interrupt.

Default key is `Alt` + `Shift` + `x`

This script tries to stop all python programs by sending the os-interrupt signal to all programs.



## License

MIT
