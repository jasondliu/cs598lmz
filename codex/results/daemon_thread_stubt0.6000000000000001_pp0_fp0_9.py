import sys, threading

def run():
	os.system("python manage.py runserver")

def manage():
	os.system("python manage.py")

def make():
	os.system("python manage.py makemigrations")

def migrate():
	os.system("python manage.py migrate")

def main():
	print("1.runserver")
	print("2.manage")
	print("3.makemigrations")
	print("4.migrate")
	print("5.exit")
	while True:
		a = input()
		if a == "1":
			t = threading.Thread(target=run)
			t.setDaemon(True)
			t.start()
		elif a == "2":
			t = threading.Thread(target=manage)
			t.setDaemon(True)
			t.start()
		elif a == "3":
			t = threading.Thread(target=make)
			t.setDaemon(True)
