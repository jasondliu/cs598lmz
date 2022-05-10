import sys, threading

def run():
	pygame.mixer.init()
	pygame.mixer.music.load("record.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

if __name__ == '__main__':
	thread = threading.Thread(target=run)
	thread.daemon = True
	thread.start()

	while True:
		pass
