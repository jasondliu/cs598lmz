import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("ANTIVIRUS")
pyttsx3.speak("hello user iam  virusscanner")
pyttsx3.speak("how may i help u")
while True:
	print("chat with me with your requirements:",end='')
	p=input()

	if "run" in p or "execute" in p or "launch" in p or "start" in p and "chrome" in p:
		if "dont" in p or  "do not" in p or "not" in p and ("run" in p or "start" in p or "execute" in p or "launch" in p) and ("chrome" in p):
			print("ok i will not run chrome")
			pyttsx3.speak("ok i will not run chrome")
			continue
		else:
			pyttsx3.speak("opening chrome")
			#webbrowser.open("www.google.com")
			os.system("chrome")
			py
