import sys, threading

def run():
	os.chdir("/home/speedy/Pictures")
	a = input("Would you like to use ImageMagick? (y/n) ")
	end = ""
	if a == "y":
		while end == "":
			print("Use: convert image.jpg image.png to convert a file.")
			sys.stdout.write(">>>")
			sys.stdout.flush()
			a = input()
			if a == "exit":
				end = 1
			else:
				os.system("convert " + a)
	else:
		while end == "":
			print("Version 1.2")
			print("Commands:")
			print("  1) Help  5) Open in Image Viewer  8) Convert to BMP")
			print("  2) Exit  6) Convert to JPEG      9) Convert to PNG")
			print("  3) Info  7) Convert to TIFF")
			print("
