import sys, threading

def run():
	p = Program(size=size)

	# set the screen to color 2
	p.set(0, 2)

	i = 0
	# the screen is an array, so keep running until
	# we hit the end of the array
	while i < size:
		# if we hit the left wall,
		# reverse direction
		if p[i] == 8:
			p.up()

		# if we hit the right wall,
		# reverse direction
		if p[i] == 3:
			p.down()

		# move the position
		i = p.move()[0]

		# display the output
		p.view()
		time.sleep(interval)

configuration = input("Please enter your configuration setting: ")

size = 8
interval = 0.2

if configuration == "1":
	size = 16
	interval = 0.1
elif configuration == "2":
	size = 8
	interval = 0.03
elif configuration == "3":
